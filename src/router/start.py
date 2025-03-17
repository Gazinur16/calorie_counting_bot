import logging

from aiogram import types, Router
from aiogram.filters import Command, or_f, StateFilter

from src.blank.public import PublicTgBotBlank
from src.core.const import PublicTgBotCommands
from src.filter.filter_ import TextFilterTgBotFilter, IsPrivateChatTgBotFilter

router = Router()
_logger = logging.getLogger(__name__)

@router.message(
    or_f(
        Command(PublicTgBotCommands.start),
        TextFilterTgBotFilter([
            "начать",
            "старт",
            "привет",
            "запуск",
            "start",
        ], ignore_case=True)
    ),
    IsPrivateChatTgBotFilter(),
    StateFilter("*")
)
async def _(m: types.Message, **kwargs):
    await m.answer(
        text=PublicTgBotBlank.start()
    )

