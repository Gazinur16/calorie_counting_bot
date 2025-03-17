from aiogram import types, Router
from aiogram.filters import Command, or_f, StateFilter

from src.blank.public import PublicTgBotBlank
from src.core.const import PublicTgBotCommands
from src.filter.filter_ import TextFilterTgBotFilter, IsPrivateChatTgBotFilter

router = Router()


@router.message(
    or_f(
        Command(PublicTgBotCommands.about),
        TextFilterTgBotFilter([
            "about",
            "о проекте",
            "что за бот",
            "что за проект"
        ], ignore_case=True)
    ),
    IsPrivateChatTgBotFilter(),
    StateFilter("*")
)
async def _(m: types.Message, **kwargs):
    await m.answer(
        text=PublicTgBotBlank.about()
    )