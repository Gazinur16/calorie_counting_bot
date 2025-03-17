import asyncio
import json

from openai.types.chat import ChatCompletion

from src.core.const import PROMPT_FOR_ANALIZ_TEXT
from src.core.util import get_easy_openai


async def define_ingredients_by_text(*, str_from_user: str) -> list[dict[str, int]]:
    easy_openai = get_easy_openai()

    response: ChatCompletion = easy_openai.open_ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PROMPT_FOR_ANALIZ_TEXT},
            {"role": "user", "content": str_from_user}
        ],
        n=1,
        temperature=0.1,
        top_p=0.9,
        timeout=60,
        max_tokens=300
    )

    response_text = response.choices[0].message.content.strip()
    response_text = response_text.removeprefix("\"").removesuffix("\"").strip()
    response_text = response_text.removeprefix("'").removesuffix("'").strip()
    response_text = response_text.removeprefix("```").removesuffix("```").strip()

    return json.loads(response_text)


async def __async_example():
    res = await define_ingredients_by_text(
        str_from_user="Яблоко, и две шоколадных конфетки"
    )
    print(res)


if __name__ == '__main__':
    asyncio.run(__async_example())