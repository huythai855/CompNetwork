import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
url = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + OPENAI_API_KEY
           }
def ask_openai(question):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7
    }
    r = requests.post(url, json=payload, headers=headers)
    json_response = r.json()
    return json_response['choices'][0]['message']['content'][2:]
