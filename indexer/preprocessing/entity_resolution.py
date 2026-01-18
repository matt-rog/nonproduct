from pydantic import BaseModel
from typing import List, Optional
from agent import Agent
import json
import search

class Product(BaseModel):
    name: str

class Company(BaseModel):
    name: str

class EntityClassificationResponse(BaseModel):
    product: Optional[Product]
    companies: Optional[List[Company]]

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

    completion = agent.client.chat.completions.create(
        model=agent.model,
        messages=[
            {
                "role": "user",
                "content": entity_classification_prompt
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "entity_classification",
                "schema": EntityClassificationResponse.model_json_schema()
            }
        }
    )
    
    print(completion.choices[0].message.content)