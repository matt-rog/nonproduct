from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
vllm_url = os.getenv("VLLM_URL")

class Agent():
    def __init__(self):
        self.client = OpenAI(
            base_url=vllm_url,
            api_key="-"
        )

        self.model = self.client.models.list().data[-1].id