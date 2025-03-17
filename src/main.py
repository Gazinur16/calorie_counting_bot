import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.core import on_error
from src.core.settings import get_settings
from src.core.setup_logging import setup_logging
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.core.util import create_tg_bot
from src.event.on_shutdown import OnShutdownTgBotEvent
from src.event.on_startup import OnStartupTgBotEvent
from src.router.router import public_router


def main():
    setup_logging()

    settings = get_settings()
    tg_bot = create_tg_bot()

    transmitted_tg_bot_data = TransmittedTgBotData(
        settings=settings,
        tg_bot=tg_bot
    )

    tg_dp = Dispatcher(
        storage=MemoryStorage(),
        settings=get_settings(),
        transmitted_tg_bot_data=transmitted_tg_bot_data
    )

    tg_dp.startup.register(OnStartupTgBotEvent(transmitted_tg_bot_data=transmitted_tg_bot_data).on_startup)
    tg_dp.shutdown.register(OnShutdownTgBotEvent(transmitted_tg_bot_data=transmitted_tg_bot_data).on_shutdown)

    # tg_dp.include_router(on_error.router)
    tg_dp.include_router(public_router)

    asyncio.run(tg_dp.start_polling(tg_bot))


if __name__ == '__main__':
    main()
