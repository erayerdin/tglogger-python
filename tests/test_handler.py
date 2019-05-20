import os

import pytest
import requests


class TestTelegramHandler:
    def test_emit_return_type(self, telegram_handler, log_record_factory):
        log_record = log_record_factory()

        responses = telegram_handler.emit(log_record)
        assert isinstance(responses, dict)

        for value in responses.values():
            assert isinstance(value, requests.Response) or value is None
