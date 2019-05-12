import json
import logging
import typing

import pytest
import requests_mock

import tglogger.formatter
import tglogger.handler
import tglogger.request


@pytest.fixture
def mock_adapter() -> requests_mock.Adapter:
    return requests_mock.Adapter()


@pytest.fixture
def bot_session(mock_adapter) -> tglogger.request.BotSession:
    session = tglogger.request.BotSession("0")
    session.mount("mock", mock_adapter)
    session._is_mocked = True
    return session


@pytest.fixture
def bot_request_factory(bot_session) -> callable:
    def factory(method_name: str) -> tglogger.request.BotRequest:
        return tglogger.request.BotRequest(bot_session, method_name)

    return factory


@pytest.fixture
def bot_send_message_request(
    bot_session
) -> tglogger.request.SendMessageRequest:
    return tglogger.request.SendMessageRequest(bot_session, 1, "foo")


@pytest.fixture
def request_body_factory() -> callable:
    def factory(request: requests_mock.request.requests.Request) -> dict:
        return json.loads(request.body.decode("utf-8"))

    return factory


@pytest.fixture(scope="module")
def logger() -> logging.Logger:
    return logging.getLogger("example.logger")


@pytest.fixture(scope="module")
def log_record_factory(
    logger: logging.Logger
) -> typing.Callable[[], logging.LogRecord]:
    def factory(**kwargs) -> logging.LogRecord:
        return logging.LogRecord(
            name=kwargs.get("name", logger.name),
            level=kwargs.get("level", logging.ERROR),
            pathname=kwargs.get("pathname", "/foo/bar/baz.py"),
            lineno=kwargs.get("lineno", 1),
            msg=kwargs.get("msg", "An error occured."),
            args=kwargs.get("args", ()),
            exc_info=(None, None, None),
            func=kwargs.get("func", "foo_bar_baz"),
            sinfo="An error occured in whatever.",
        )

    return factory


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
