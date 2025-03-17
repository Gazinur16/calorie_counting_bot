import logging

from src.business_service.notify_admins import notify_admins
from src.core.transmitted_tg_bot_data import TransmittedTgBotData

_logger = logging.getLogger(__name__)


class OnShutdownTgBotEvent:
    def __init__(self, *, transmitted_tg_bot_data: TransmittedTgBotData):
        self._logger = logging.getLogger(self.__class__.__name__)
        self.transmitted_tg_bot_data = transmitted_tg_bot_data

    async def on_shutdown(self, *args, **kwargs):
        _logger.info("on_shutdown start")

        await notify_admins(
            tg_bot=self.transmitted_tg_bot_data.tg_bot,
            text="Shutdown"
        )

        _logger.info("on_shutdown was done")
