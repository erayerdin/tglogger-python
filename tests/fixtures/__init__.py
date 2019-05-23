import json
import logging
import typing

import pytest
import requests_mock

import tglogger.formatter
import tglogger.handler
import tglogger.request

from .logging import *
from .resource import *


@pytest.fixture(scope="module")
def telegram_formatter() -> tglogger.formatter.TelegramFormatter:
    return tglogger.formatter.TelegramFormatter()


@pytest.fixture(scope="module")
def telegram_handler(telegram_formatter) -> tglogger.handler.TelegramHandler:
    handler = tglogger.handler.TelegramHandler(bot_token="1", receiver="2")
    handler.setFormatter(telegram_formatter)
    return handler


@pytest.fixture(scope="module")
def telegram_logger(telegram_handler, telegram_formatter) -> logging.Logger:
    logger = logging.getLogger("test logger")
    logger.addHandler(telegram_handler)
    return logger
