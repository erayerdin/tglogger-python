import uuid

import pytest
import requests


def test_log_record_uuid(log_record_factory):
    log_record = log_record_factory()
    assert isinstance(log_record.uuid, uuid.UUID)


# Telegram Handler Tests
def test_handler_emit_return_type(telegram_handler, log_record_factory):
    log_record = log_record_factory()

    responses = telegram_handler.emit(log_record)
    assert isinstance(responses, dict)

    for value in responses.values():
        assert isinstance(value, requests.Response) or value is None


def test_invalid_bot_exception():
    from tglogger.handler import TelegramHandler, InvalidBotError

    with pytest.raises(InvalidBotError):
        handler = TelegramHandler(
            bot_token="foo", receiver="bar"
        )  # no such bot
