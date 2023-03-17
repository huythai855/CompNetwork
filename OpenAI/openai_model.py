import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.organization = os.environ.get("OPENAI_ORGANIZATION_ID")
openai.api_key = os.environ.get("OPENAI_API_KEY")

print(openai.organization)
print(openai.api_key)

openai.Model.list()


