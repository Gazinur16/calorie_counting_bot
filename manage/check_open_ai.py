import os

from openai import OpenAI
from openai.types.chat import ChatCompletion
from dotenv import load_dotenv

load_dotenv()
PROXY_API_KEY = os.getenv("PROXY_API_KEY")

def command():
    client = OpenAI(
        api_key=PROXY_API_KEY,
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты помогающий ассистент для подсчета калорий"
                )
            },
            {
                "role": "user",
                "content": "Привет, ты живой?"
            },
        ],
    )

    res = response.choices[0].message.content.strip()
    print(res)

if __name__ == '__main__':
    command()
