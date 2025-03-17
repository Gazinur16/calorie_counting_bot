import asyncio
import logging
from datetime import timedelta

from aiogram import Bot
from aiogram.exceptions import AiogramError
from emoji import emojize


from arpakitlib.ar_str_util import remove_tags_and_html
from src.core.util import create_tg_bot
from src.core.settings import get_settings

_logger = logging.getLogger(__name__)
settings = get_settings()

async def notify_admins(*, text: str, tg_bot: Bot):
    text = emojize(text.strip())

    full_text = f"<b>Уведомление для администраторов</b>"
    full_text += f"\n\n{text}"

    for admin_tg_id in settings.admin_tg_ids:
        try:
            await tg_bot.send_message(
                chat_id=admin_tg_id,
                text=full_text,
                request_timeout=int(timedelta(seconds=3).total_seconds())
            )
        except AiogramError:
            try:
                await tg_bot.send_message(
                    chat_id=admin_tg_id,
                    text=remove_tags_and_html(full_text),
                    request_timeout=int(timedelta(seconds=3).total_seconds())
                )
            except AiogramError as e:
                _logger.error(e)


async def __async_example():
    tg_bot = create_tg_bot()
    await notify_admins(
        text="Hello",
        tg_bot=tg_bot
    )
    await tg_bot.session.close()


if __name__ == '__main__':
    asyncio.run(__async_example())
