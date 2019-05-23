import re

import pytest

import tglogger.request


def test_isinstance(send_log_responses):
    assert isinstance(send_log_responses, dict)


def test_length(send_log_responses):
    assert len(send_log_responses) == 3


def test_key_isinstance(send_log_responses):
    for key in send_log_responses:
        assert isinstance(key, str)


def test_value_isinstance(send_log_responses):
    for _, value in send_log_responses.items():
        assert (
            isinstance(value, tglogger.request.requests.Response)
            or value is None
        )


def test_generic_info_response_key_name(send_log_responses):
    assert "generic_info_response" in send_log_responses


def test_stack_trace_response_key_name(send_log_responses):
    assert "stack_trace_response" in send_log_responses


def test_django_settings_response_key_name(send_log_responses):
    assert "django_settings_response" in send_log_responses
