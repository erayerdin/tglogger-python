import re
from urllib.parse import parse_qs

import pytest

import tglogger.request


@pytest.fixture
def send_log_responses(
    telegram_handler, log_record_factory, requests_mock, read_test_resource
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

    log_record = log_record_factory()
    return tglogger.request.send_log(telegram_handler, log_record, 1)


@pytest.fixture
def generic_info_response(send_log_responses):
    return send_log_responses["generic_info_response"]


@pytest.fixture
def generic_info_request(generic_info_response):
    return generic_info_response.request


@pytest.fixture
def generic_info_request_body(generic_info_request):
    return parse_qs(generic_info_request.body)


class TestSendLogReturn:
    def test_isinstance(self, send_log_responses):
        assert isinstance(send_log_responses, dict)

    def test_length(self, send_log_responses):
        assert len(send_log_responses) == 3

    def test_key_isinstance(self, send_log_responses):
        for key in send_log_responses:
            assert isinstance(key, str)

    def test_value_isinstance(self, send_log_responses):
        for _, value in send_log_responses.items():
            assert (
                isinstance(value, tglogger.request.requests.Response)
                or value is None
            )

    def test_generic_info_response_key_name(self, send_log_responses):
        assert "generic_info_response" in send_log_responses

    def test_stack_trace_response_key_name(self, send_log_responses):
        assert "stack_trace_response" in send_log_responses

    def test_django_settings_response_key_name(self, send_log_responses):
        assert "django_settings_response" in send_log_responses


class TestSendLogGenericInfoRequest:
    def test_body_chat_id(self, generic_info_request_body):
        assert generic_info_request_body["chat_id"][0] == "1"

    def test_body_parse_mode(self, generic_info_request_body):
        assert generic_info_request_body["parse_mode"][0] == "markdown"

    def test_body_text(self, generic_info_request_body):
        assert "text" in generic_info_request_body
