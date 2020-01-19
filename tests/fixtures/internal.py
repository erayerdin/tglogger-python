import logging

import pytest

import tglogger.formatter
import tglogger.handler
import tglogger.request


@pytest.fixture
def telegram_formatter() -> tglogger.formatter.TelegramFormatter:
    return tglogger.formatter.TelegramFormatter()


@pytest.fixture
def telegram_handler(telegram_formatter) -> tglogger.handler.TelegramHandler:
    handler = tglogger.handler.TelegramHandler(
        bot_token="1", receiver="2", bypass_auth=True
    )
    handler.setFormatter(telegram_formatter)
    return handler


@pytest.fixture
def telegram_logger(telegram_handler, telegram_formatter) -> logging.Logger:
    logger = logging.getLogger("test logger")
    logger.addHandler(telegram_handler)
    return logger
