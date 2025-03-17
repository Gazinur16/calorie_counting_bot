import asyncio
import logging

from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest, AiogramError
from aiogram.types import ErrorEvent

from src.blank.public import PublicTgBotBlank
from src.business_service.notify_admins import notify_admins
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.kb.inline import support_ikb

router = Router()

_logger = logging.getLogger(__name__)


#TODO это не работет
@router.error(F.update.message.as_("m"))
async def _(error_event: ErrorEvent, m: types.Message, **kwargs):
    _logger.exception(error_event.exception)

    transmitted_tg_bot_data: TransmittedTgBotData | None = kwargs.get("transmitted_tg_bot_data")

    try:
        await m.answer(
            text=PublicTgBotBlank.error(),
            reply_markup=support_ikb()
        )
    except AiogramError as e:
        _logger.error(e)

    if transmitted_tg_bot_data and transmitted_tg_bot_data.tg_bot:

        text = f"Произошла ошибка у пользователя"
        text += f"\n\nevent_type: <code>{error_event.update.event_type}</code>"
        text += f"\n\nerror: {error_event.exception}"
        if transmitted_tg_bot_data.user_dbm is not None:
            text += f"\n\nuser_tg_id=<code>{transmitted_tg_bot_data.user_dbm.tg_id}</code>"
        else:
            text += f"\n\nuser_tg_id=None"

        _ = asyncio.create_task(notify_admins(
            tg_bot=transmitted_tg_bot_data.tg_bot,
            text=text
        ))


@router.error(F.update.callback_query.as_("cq"))
async def _(error_event: ErrorEvent, cq: types.CallbackQuery, **kwargs):
    _logger.error(error_event.exception)

    transmitted_tg_bot_data: TransmittedTgBotData | None = kwargs.get("transmitted_tg_bot_data")

    try:
        await cq.answer()
    except AiogramError:
        pass

    if isinstance(error_event.exception, TelegramBadRequest):
        if (
                error_event.exception.message
                and "message is not modified".lower().strip() in error_event.exception.message.lower().strip()
        ):
            return

    _logger.exception(error_event.exception)

    try:
        await cq.message.edit_reply_markup(reply_markup=None)
    except AiogramError:
        pass

    try:
        await cq.message.answer(
            text=PublicTgBotBlank.error(),
            reply_markup=support_ikb()
        )
    except AiogramError:
        pass

    if transmitted_tg_bot_data and transmitted_tg_bot_data.tg_bot:

        text = f"Произошла ошибка у пользователя"
        text += f"\n\nevent_type: <code>{error_event.update.event_type}</code>"
        text += f"\n\ncq_data: {cq.data}"
        text += f"\n\nerror: {error_event.exception}"
        if transmitted_tg_bot_data.user_dbm is not None:
            text += f"\n\nuser_tg_id=<code>{transmitted_tg_bot_data.user_dbm.tg_id}</code>"
        else:
            text += f"\n\nuser_tg_id=None"

        _ = asyncio.create_task(notify_admins(
            tg_bot=transmitted_tg_bot_data.tg_bot,
            text=text
        ))
