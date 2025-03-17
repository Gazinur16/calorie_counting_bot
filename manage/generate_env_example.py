import logging
import os.path

from arpakitlib.ar_settings_util import generate_env_example
from src.core.const import BASE_DIRPATH
from src.core.settings import Settings
from src.core.setup_logging import setup_logging

_logger = logging.getLogger(__name__)


def command():
    setup_logging()
    env_example = generate_env_example(settings_class=Settings)
    _logger.info(env_example)
    with open(os.path.join(BASE_DIRPATH, ".env_example"), mode="w") as f:
        f.write(env_example)
    _logger.info("env example was generated")


if __name__ == '__main__':
    command()
