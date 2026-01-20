from dotenv import load_dotenv
from openai import OpenAI
from trace import Trace
import os

load_dotenv()
vllm_url = os.getenv("VLLM_URL")

class Agent():
    def __init__(self):
        self.client = OpenAI(
            base_url=vllm_url,
            api_key="-"
        )

        self.model = self.client.models.list().data[0].id

    def structured_response(self, messages, schema, schema_name):

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        Trace.log(["unstructured", {"input": messages, "output": completion.choices[0].message.content}])

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": schema_name,
                    "schema": schema
                }
            }
        )

        Trace.log(["structured", {"input": messages, "output": completion.choices[0].message.content}])

        return completion.choices[0].message.content