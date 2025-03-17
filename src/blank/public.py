from emoji import emojize

from src.core.const import PublicTgBotCommands


class PublicTgBotBlank:

    @classmethod
    def command_to_desc(cls) -> dict[str, str]:
        return {
            PublicTgBotCommands.support: emojize(":red_heart: Поддержка"),
            PublicTgBotCommands.about: emojize(":information: Подробнее"),
            PublicTgBotCommands.start: emojize(":rocket: Начать")
        }

    @classmethod
    def error(cls) -> str:
        res = ":warning: <b>Произошла неполадка</b> :warning:"
        res += "\n\n:wrench: Мы уже исправляем её"
        res += (
            f"\n\n— Для оперативного решения вопросы обратитесь"
            f" в <a href='https://t.me/nurtdinov_gt'>поддержку</a>"
        )
        return emojize(string=res.strip())

    @classmethod
    def but_support(cls) -> str:
        return emojize(string=":red_heart: Поддержка")

    @classmethod
    def start(cls) -> str:
        return emojize(string=":waving_hand: Привет! Отправь фото блюда, и я расскажу его калорийность и БЖУ!")

    @classmethod
    def support(cls) -> str:
        res = f":otter: По всем вопросам обращайтесь в <a href='https://t.me/nurtdinov_gt'>поддержку</a>"
        res += f"\n\n:link: https://t.me/nurtdinov_gt"
        return emojize(string=res.strip(), language="alias")

    @classmethod
    def about(cls) -> str:
        res = f":hamburger: <b>Информация о боте:</b>\n"
        res += f"\nЭтот бот поможет Вам определять их калорийность блюд по их фотографии."
        res += f"\n\n<b>Возможности бота:</b>"
        res += f"\n- Распознавание продуктов на фото и определение состава блюда"
        res += f"\n- Генерация таблицы с питательной ценностью (калории, белки, жиры, углеводы)"
        res += f"\n- Работа с изображениями и текстовыми запросами"
        res += f"\n\n<b>Как использовать бота?</b>"
        res += f"\n1. Отправьте фото блюда или введите его название вручную."
        res += f"\n2. Бот определит ингредиенты и рассчитает калорийность."
        res += f"\n3. Вы получите таблицу с питательной ценностью."
        res += f"\n\n:link: <b>Поддержка:</b> https://t.me/nurtdinov_gt"

        return emojize(string=res.strip())

    @classmethod
    def image_is_loaded(cls) -> str:
        res = f":paperclip: <b>Изображение загружено!</b>"
        res += f"\n\n— Начинаю обработку, подождите немного..."
        return emojize(string=res.strip())

    @classmethod
    def request_is_accepted(cls) -> str:
        res = f":spiral_notepad: <b>Ваш запрос принят!</b>"
        res += f"\n\n— Начинаю обработку, подождите немного..."
        return emojize(string=res.strip())

    @classmethod
    def failed_to_load_the_image(cls) -> str:
        res = f":warning: <b>Не удалось загрузить изображение.</b>"
        res += f"\n\n— Пожалуйста, попробуйте еще раз"
        return emojize(string=res.strip())

    @classmethod
    def failed_to_process_the_msg(cls) -> str:
        res = f":warning: <b>Не удалось корректно обработать ваше сообщение</b>"
        res += f"\n\n— Пожалуйста, попробуйте еще раз"
        return emojize(string=res.strip())

    @classmethod
    def not_found_the_food_in_photo(cls) -> str:
        res = f":sad_but_relieved_face: <b>Не удалось найти блюдо на фото</b>"
        res += f"\n\n— Пожалуйста, убедитесь что блюдо на изображении хорошо видно и попробуйте загрузить фото снова."
        return emojize(string=res.strip())


def __example():
    pass


if __name__ == '__main__':
    __example()
