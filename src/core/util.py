from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode

from httpx import Timeout
from functools import lru_cache
from arpakitlib.ar_openai_api_client_util import OpenAIAPIClient, OpenAI, AsyncOpenAI

from src.core.settings import get_settings


def create_tg_bot() -> Bot:
    _tg_bot_session: AiohttpSession | None = None
    tg_bot = Bot(
        token=get_settings().tg_bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            disable_notification=False,
            link_preview_is_disabled=True
        ),
        session=_tg_bot_session
    )
    return tg_bot


def create_easy_openai() -> OpenAIAPIClient:
    return OpenAIAPIClient(
        open_ai=OpenAI(
            api_key=get_settings().openai_api_key,
            base_url=get_settings().openai_api_base_url,
            timeout=Timeout(
                timeout=60,
                connect=15,
                read=60,
                write=60,
                pool=15
            )
        ),
        async_open_ai=AsyncOpenAI(
            api_key=get_settings().openai_api_key,
            base_url=get_settings().openai_api_base_url
        )
    )


@lru_cache()
def get_easy_openai() -> OpenAIAPIClient:
    return create_easy_openai()

# def create_media_file_storage_in_dir() -> FileStorageInDir:
#     from src.core.settings import get_settings
#     return FileStorageInDir(dirpath=get_settings().media_dirpath)
#
#
# @lru_cache()
# def get_media_file_storage_in_dir() -> FileStorageInDir:
#     return create_media_file_storage_in_dir()
#
#
# def now_local_dt() -> datetime:
#     return datetime.now(tz=pytz.timezone(get_settings().local_timezone))
