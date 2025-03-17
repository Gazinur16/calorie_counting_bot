import asyncio
import logging

from src.business_service.notify_admins import notify_admins
from src.business_service.set_tg_bot_commands import set_public_tg_bot_commands
from src.core.transmitted_tg_bot_data import TransmittedTgBotData

_logger = logging.getLogger(__name__)


class OnStartupTgBotEvent:
    def __init__(self, *, transmitted_tg_bot_data: TransmittedTgBotData):
        self._logger = logging.getLogger(self.__class__.__name__)
        self.transmitted_tg_bot_data = transmitted_tg_bot_data

    async def on_startup(self, *args, **kwargs):
        _logger.info("on_startup start")

        if self.transmitted_tg_bot_data.settings.tg_bot_drop_pending_updates:
            await self.transmitted_tg_bot_data.tg_bot.delete_webhook(drop_pending_updates=True)
            _logger.info("tg bot pending updates were dropped")

        if self.transmitted_tg_bot_data.settings.tg_bot_set_commands:
            await set_public_tg_bot_commands(tg_bot=self.transmitted_tg_bot_data.tg_bot)

        _ = asyncio.create_task(notify_admins(
            tg_bot=self.transmitted_tg_bot_data.tg_bot,
            text="Startup"
        ))

        _logger.info("on_startup was done")
