import pytest


def test_request_body_chat_id(generic_info_request_body):
    assert generic_info_request_body["chat_id"][0] == "1"


def test_request_body_parse_mode(generic_info_request_body):
    assert generic_info_request_body["parse_mode"][0] == "markdown"


def test_request_body_text(generic_info_request_body):
    assert "text" in generic_info_request_body
