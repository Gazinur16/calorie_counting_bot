import logging
import uuid

from aiogram import types, Router
from aiogram.exceptions import AiogramError
from arpakitlib.ar_type_util import raise_for_type

from src.blank.public import PublicTgBotBlank
from src.business_service.calculate_total_line import get_total_line
from src.business_service.define_ingredients_by_text import define_ingredients_by_text
from src.business_service.generate_image import generate_nutrition_image
from src.filter.filter_ import TextFilterTgBotFilter, IsPrivateChatTgBotFilter

router = Router()
_logger = logging.getLogger(__name__)

@router.message(IsPrivateChatTgBotFilter())
async def _(
        m: types.Message,
        **kwargs
):
    if len(m.text) > 3:
        raise_for_type(m.text, str)
        str_from_user_ = m.text.strip()
    else:
        try:
            await m.answer(text=PublicTgBotBlank.failed_to_process_the_msg())
        except AiogramError as e:
            _logger.error(e)
        return

    try:
        msg_about_rqst_accepted = await m.answer(text=PublicTgBotBlank.request_is_accepted())
    except AiogramError as e:
        msg_about_rqst_accepted = None
        _logger.error(e)

    ingredients_on_photo = await define_ingredients_by_text(str_from_user=str_from_user_)
    raise_for_type(ingredients_on_photo, list)

    if not ingredients_on_photo:
        await msg_about_rqst_accepted.edit_text(text=PublicTgBotBlank.not_found_the_food_in_photo())
        return

    img_buffer = generate_nutrition_image(ingredients=ingredients_on_photo,
                                          total_row=get_total_line(ingredients_on_photo=ingredients_on_photo))
    photo_result_table = types.BufferedInputFile(img_buffer.getvalue(), filename=f"{uuid.uuid4().hex[:12]}.jpg")

    try:
        if msg_about_rqst_accepted:
            await msg_about_rqst_accepted.delete()

        await m.answer_photo(photo=photo_result_table, caption="📊 Анализ описания:")
    except AiogramError as e:
        await msg_about_rqst_accepted.edit_text(text=PublicTgBotBlank.not_found_the_food_in_photo())
        _logger.error(e)