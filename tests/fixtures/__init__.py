import json
import logging
import typing

import pytest
import requests_mock

import tglogger.formatter
import tglogger.handler
import tglogger.request

from .resource import *


@pytest.fixture(scope="module")
def logger() -> logging.Logger:
    return logging.getLogger("example.logger")


@pytest.fixture(scope="module")
def log_record_factory(
    logger: logging.Logger
) -> typing.Callable[[], logging.LogRecord]:
    def factory(**kwargs) -> logging.LogRecord:
        internal_factory = logging.getLogRecordFactory()
        return internal_factory(
            name=kwargs.get("name", logger.name),
            level=kwargs.get("level", logging.ERROR),
            pathname=kwargs.get("pathname", "/foo/bar/baz.py"),
            lineno=kwargs.get("lineno", 1),
            msg=kwargs.get("msg", "An error occured."),
            args=kwargs.get("args", ()),
            exc_info=kwargs.get("exc_info", None),
            func=kwargs.get("func", "foo_bar_baz"),
            sinfo="An error occured in whatever.",
        )

    return factory


@pytest.fixture(scope="module")
def exception_log_record(log_record_factory):
    from collections import namedtuple

    return log_record_factory(
        exc_info=(
            Exception,
            Exception("foo"),
            namedtuple(
                "fake_tb", ("tb_frame", "tb_lasti", "tb_lineno", "tb_next")
            ),  # ref: https://stackoverflow.com/a/49561567/2926992
        )
    )


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
