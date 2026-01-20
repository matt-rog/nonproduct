from pydantic import BaseModel
from typing import List, Optional
from agent import Agent
from trace import Trace
import json
import search

class Product(BaseModel):
    name: str

class Company(BaseModel):
    name: str

class EntityClassificationResponse(BaseModel):
    product: Optional[Product]
    companies: List[Company]

# ER determines if the query is a product or a company. 
# If it is a product, it searches for and fills out any missing company information.
# The new product entity, and any new company entities, are then queued for claim resolution.
def resolve(term):
    init_context = search.search(term)
    print(init_context)
    
    # Classify entity, extracting relevant companies
    agent = Agent()
    print(agent.model)

    with open('prompts/entity_classification.md', 'r') as f:
        entity_classification_prompt = f.read().replace("{term}", term).replace("{init_context}", json.dumps(init_context))

    Trace.log("Starting entity classification")
    response = agent.structured_response(
        [
            {
                "role": "user",
                "content": entity_classification_prompt
            }
        ],
        EntityClassificationResponse.model_json_schema(),
        "entity_classification"
    )

    print(response)