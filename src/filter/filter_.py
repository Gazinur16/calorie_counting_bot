from typing import Iterable

import aiogram.types
from aiogram.filters import Filter

from arpakitlib.ar_type_util import raise_for_type


class TextFilterTgBotFilter(Filter):

    def __init__(
            self,
            *texts: str | Iterable[str],
            ignore_case: bool = True
    ) -> None:
        self.ignore_case = ignore_case
        self.texts = set()

        for text in texts:

            if isinstance(text, str):
                if ignore_case is True:
                    text = text.lower()
                text = text.strip()
                self.texts.add(text)

            elif isinstance(text, Iterable):
                for text_ in text:
                    raise_for_type(text_, str)
                    if ignore_case is True:
                        text_ = text_.lower()
                    text_ = text_.strip()
                    self.texts.add(text_)

            else:
                raise TypeError(f"text has bad type = {type(text)}")

    async def __call__(self, message: aiogram.types.Message, *args, **kwargs) -> bool:
        raise_for_type(message, aiogram.types.Message)

        if message.text is None:
            return False

        text = message.text.strip()
        if self.ignore_case is True:
            text = text.lower()

        return text in self.texts


class IsPrivateChatTgBotFilter(Filter):
    async def __call__(self, update: aiogram.types.Message | aiogram.types.CallbackQuery) -> bool:
        if isinstance(update, aiogram.types.Message):
            return update.chat.type == aiogram.enums.ChatType.PRIVATE
        elif isinstance(update, aiogram.types.CallbackQuery):
            return update.message.chat.type == aiogram.enums.ChatType.PRIVATE
        else:
            return False


class IsImageFileFilter(Filter):
    async def __call__(self, message: aiogram.types.Message) -> bool:
        return bool(
            message.photo or
            (message.document and message.document.mime_type.startswith("image/"))
        )
