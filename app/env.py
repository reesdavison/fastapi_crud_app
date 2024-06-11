import sys
from functools import lru_cache

from dotenv import dotenv_values

from .config import AppConfig


@lru_cache
def get_app_config() -> AppConfig:
    if "pytest" in sys.modules:
        return get_test_config()
    config = AppConfig.model_validate(dotenv_values(".env"))
    return config


def get_test_config() -> AppConfig:
    # we setup the DB separately
    config = AppConfig(DATABASE_URL="")
    return config
