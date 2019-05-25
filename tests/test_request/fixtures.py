import re
from urllib.parse import parse_qs

import pytest

import tglogger.request


# send_log
@pytest.fixture
def api_mock(requests_mock, read_test_resource):
    send_message_rule = re.compile(
        "https:\/\/api.telegram.org\/bot.+\/sendMessage"
    )
    send_document_rule = re.compile(
        "https:\/\/api.telegram.org\/bot.+\/sendDocument"
    )

    requests_mock.register_uri(
        "POST",
        send_message_rule,
        text=read_test_resource("message.response.json").read(),
    )
    requests_mock.register_uri(
        "POST",
        send_document_rule,
        text=read_test_resource("message.response.json").read(),
    )


@pytest.fixture
def send_log_response(telegram_handler, log_record_factory, api_mock):
    log_record = log_record_factory()
    return tglogger.request.send_log(telegram_handler, log_record, 1)


@pytest.fixture
def send_log_exception_response(
    telegram_handler, exception_log_record, api_mock
):
    return tglogger.request.send_log(telegram_handler, exception_log_record, 1)


# Generic Info


@pytest.fixture
def send_log_request(send_log_response):
    return send_log_response.request


@pytest.fixture
def send_log_request_body(send_log_request):
    return parse_qs(send_log_request.body)


@pytest.fixture
def send_log_exception_request(send_log_exception_response):
    return send_log_exception_response.request


@pytest.fixture
def send_log_exception_request_body(send_log_exception_request):
    return send_log_exception_request.body
