import re
from urllib.parse import parse_qs

import pytest

import tglogger.request

# send_log


@pytest.fixture
def send_log_response(
    telegram_handler, exception_log_record, requests_mock, read_test_resource
):
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

    return tglogger.request.send_log(telegram_handler, exception_log_record, 1)


# Generic Info


@pytest.fixture
def send_log_request(send_log_response):
    return send_log_response.request


@pytest.fixture
def send_log_request_body(send_log_request):
    return parse_qs(send_log_request.body)
