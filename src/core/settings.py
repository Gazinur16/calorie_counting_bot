import logging
import os
from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from arpakitlib.ar_json_util import safely_transfer_obj_to_json_str

from src.core.const import BASE_DIRPATH, ENV_FILEPATH

_logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    model_config = ConfigDict(extra="ignore")

    prod_mode: bool = False

    tg_bot_token: str

    tg_bot_set_commands: bool = True

    tg_bot_drop_pending_updates: bool = True

    admin_tg_command_passwd: str = "1234"

    admin_tg_ids: list[int] = [817649215]

    openai_api_key: str | None = None
    openai_api_base_url: str | None = "https://api.proxyapi.ru/openai/v1"

    media_dirname: str = "media"
    media_dirpath: str = os.path.join(BASE_DIRPATH, media_dirname)

    log_filename: str = "story.log"
    log_filepath: str = os.path.join(BASE_DIRPATH, log_filename)

    local_timezone: str = "Asia/Yekaterinburg"


@lru_cache()
def get_settings() -> Settings:
    if os.path.exists(ENV_FILEPATH):
        return Settings(_env_file=ENV_FILEPATH, _env_file_encoding="utf-8")
    return Settings()


if __name__ == '__main__':
    print(safely_transfer_obj_to_json_str(get_settings().model_dump(mode="json")))
