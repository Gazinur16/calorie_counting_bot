import asyncio
import base64
import json

from openai.types.chat import ChatCompletion

from src.core.const import PROMPT_FOR_ANALIZ_PHOTO
from src.core.util import get_easy_openai


async def define_ingredients_by_photo(*, file_bytes: bytes, caption: str | None = None) -> list[dict[str, int]]:
    easy_openai = get_easy_openai()

    file_base64 = base64.b64encode(file_bytes).decode("utf-8")

    str_from_user = caption if caption else "Определи состав блюда"

    response: ChatCompletion = easy_openai.open_ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PROMPT_FOR_ANALIZ_PHOTO},
            {"role": "user", "content": [
                {"type": "text", "text": str_from_user},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{file_base64}"}}
            ]}
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

    print(response_text)
    return json.loads(response_text)


async def __async_example():
    file_path = "../../resource/khachapuri.png"
    with open(file_path, "rb") as file:
        file_bytes = file.read()

    res = await define_ingredients_by_photo(
        file_bytes=file_bytes
    )
    print(res)


if __name__ == '__main__':
    asyncio.run(__async_example())