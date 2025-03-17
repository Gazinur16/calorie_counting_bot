import logging
import os

from arpakitlib.ar_logging_util import setup_normal_logging
from src.core.settings import get_settings

_logging_was_setup: bool = False


def init_log_file():
    settings = get_settings()
    if not os.path.exists(settings.log_filepath):
        with open(file=settings.log_filepath, mode="w") as file:
            file.write("")


def setup_logging():
    init_log_file()
    global _logging_was_setup
    if _logging_was_setup is True:
        return
    setup_normal_logging(log_filepath=get_settings().log_filepath)
    _logging_was_setup = True


if __name__ == '__main__':
    setup_logging()
    logging.getLogger(__name__).info("Hello world")
    logging.getLogger(__name__).error("Hello world")
    logging.getLogger(__name__).error("Hello world")
