import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand

from src.blank.public import PublicTgBotBlank
from src.core.const import PublicTgBotCommands
from src.core.setup_logging import setup_logging
from src.core.util import create_tg_bot

_logger = logging.getLogger(__name__)

_public_tg_bot_commands = [
    BotCommand(
        command=PublicTgBotCommands.about,
        description=PublicTgBotBlank.command_to_desc()[PublicTgBotCommands.about]
    ),
    BotCommand(
        command=PublicTgBotCommands.support,
        description=PublicTgBotBlank.command_to_desc()[PublicTgBotCommands.support]
    ),
    BotCommand(
        command=PublicTgBotCommands.start,
        description=PublicTgBotBlank.command_to_desc()[PublicTgBotCommands.start]
    ),
]

async def set_public_tg_bot_commands(*, tg_bot: Bot):
    _logger.info(f"set_public_tg_bot_commands")
    await tg_bot.set_my_commands(commands=_public_tg_bot_commands)
    _logger.info("public tg bot commands were set")



async def __async_example():
    tg_bot = create_tg_bot()
    setup_logging()
    await set_public_tg_bot_commands(tg_bot=tg_bot)
    await tg_bot.session.close()


if __name__ == '__main__':
    asyncio.run(__async_example())
