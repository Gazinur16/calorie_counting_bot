import logging
import uuid

from aiogram import types, Router
from aiogram.exceptions import AiogramError
from arpakitlib.ar_type_util import raise_for_type

from src.blank.public import PublicTgBotBlank
from src.business_service.calculate_total_line import get_total_line
from src.business_service.define_ingredients_by_photo import define_ingredients_by_photo
from src.business_service.generate_image import generate_nutrition_image
from src.core.transmitted_tg_bot_data import TransmittedTgBotData
from src.filter.filter_ import IsImageFileFilter, IsPrivateChatTgBotFilter

router = Router()
_logger = logging.getLogger(__name__)

@router.message(IsPrivateChatTgBotFilter(), IsImageFileFilter())
async def _(
        m: types.Message,
        transmitted_tg_bot_data: TransmittedTgBotData,
        **kwargs
):
    if m.photo:
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.photo[-1].file_id)
    elif m.document and m.document.mime_type.startswith("image/"):
        tg_file = await transmitted_tg_bot_data.tg_bot.get_file(file_id=m.document.file_id)
    else:
        try:
            await m.answer(text=PublicTgBotBlank.failed_to_load_the_image())
        except AiogramError as e:
            _logger.error(e)
        return

    caption_in_photo = m.caption if m.caption else None
    file_bytes = await transmitted_tg_bot_data.tg_bot.download_file(file_path=tg_file.file_path)
    file_content = file_bytes.read()

    try:
        msg_about_image_loaded = await m.answer(text=PublicTgBotBlank.image_is_loaded())
    except AiogramError as e:
        msg_about_image_loaded = None
        _logger.error(e)

    ingredients_on_photo = await define_ingredients_by_photo(file_bytes=file_content, caption=caption_in_photo)
    raise_for_type(ingredients_on_photo, list)

    if not ingredients_on_photo:
        await msg_about_image_loaded.edit_text(text=PublicTgBotBlank.not_found_the_food_in_photo())
        return

    img_buffer = generate_nutrition_image(ingredients=ingredients_on_photo,
                                          total_row=get_total_line(ingredients_on_photo=ingredients_on_photo))
    photo_result_table = types.BufferedInputFile(img_buffer.getvalue(), filename=f"{uuid.uuid4().hex[:12]}.jpg")

    try:
        if msg_about_image_loaded:
            await msg_about_image_loaded.delete()

        await m.answer_photo(photo=photo_result_table, caption="📊 Анализ описания:")
    except AiogramError as e:
        await msg_about_image_loaded.edit_text(text=PublicTgBotBlank.not_found_the_food_in_photo())
        _logger.error(e)