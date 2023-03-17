import os
import requests
from dotenv import load_dotenv

load_dotenv()
url = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + OPENAI_API_KEY
           }

while True:
    question = input('> ')
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7
    }
    r = requests.post(url, json=payload, headers=headers)
    json_response = r.json()
    print(json_response['choices'][0]['message']['content'][2:])
