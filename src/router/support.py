from aiogram import types, Router
from aiogram.filters import Command, or_f, StateFilter

from src.filter.filter_ import TextFilterTgBotFilter, IsPrivateChatTgBotFilter
from src.blank.public import PublicTgBotBlank
from src.core.const import PublicTgBotCommands
from src.kb.inline import support_ikb

router = Router()

@router.message(
    or_f(
        Command(PublicTgBotCommands.support),
        TextFilterTgBotFilter(
            [
                PublicTgBotCommands.support,
                PublicTgBotBlank.but_support(),
                "помощь",
                "мне нужна помощь",
                "поддержка",
                "support",
                "у меня есть вопрос",
                "вопрос есть"
            ], ignore_case=True
        )
    ),
    IsPrivateChatTgBotFilter(),
    StateFilter("*")
)
async def _(m: types.Message, **kwargs):
    await m.answer(
        text=PublicTgBotBlank.support(),
        reply_markup=support_ikb()
    )
