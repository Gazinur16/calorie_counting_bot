from aiogram import Bot
from pydantic import BaseModel, ConfigDict

from src.core.settings import Settings


class TransmittedTgBotData(BaseModel):
    model_config = ConfigDict(extra="ignore", arbitrary_types_allowed=True, from_attributes=True)

    settings: Settings
    tg_bot: Bot
