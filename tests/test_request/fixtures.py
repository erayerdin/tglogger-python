import re
from urllib.parse import parse_qs

import pytest

import tglogger.request

# send_log


@pytest.fixture
def send_log_responses(
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
def generic_info_response(send_log_responses):
    return send_log_responses["generic_info_response"]


@pytest.fixture
def generic_info_request(generic_info_response):
    return generic_info_response.request


@pytest.fixture
def generic_info_request_body(generic_info_request):
    return parse_qs(generic_info_request.body)


# Stack Trace


@pytest.fixture
def stack_trace_response(send_log_responses):
    return send_log_responses["stack_trace_response"]


@pytest.fixture
def stack_trace_request(stack_trace_response):
    return stack_trace_response.request


@pytest.fixture
def stack_trace_request_body(stack_trace_request):
    return stack_trace_request.body
