import logging

from arpakit_lib.safely_transfer_to_json import safely_transfer_to_json_str
from src.core.settings import get_settings
from src.core.setup_logging import setup_logging

_logger = logging.getLogger(__name__)


def command():
    setup_logging()
    settings = get_settings()
    _logger.info(f"{settings}")
    print(safely_transfer_to_json_str(settings.model_dump(mode="json")))


if __name__ == '__main__':
    command()
