import pytest


class TestSendLogGenericInfoRequest:
    def test_body_chat_id(self, generic_info_request_body):
        assert generic_info_request_body["chat_id"][0] == "1"

    def test_body_parse_mode(self, generic_info_request_body):
        assert generic_info_request_body["parse_mode"][0] == "markdown"

    def test_body_text(self, generic_info_request_body):
        assert "text" in generic_info_request_body
