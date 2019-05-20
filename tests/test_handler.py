import importlib.util
import re

import pytest
import requests


class TestTelegramHandler:
    @pytest.mark.skipif(
        importlib.util.find_spec("django") is not None,
        reason="Will be covered in test_django.",
    )
    def test_emit_return_type(
        self,
        requests_mock,
        read_test_resource,
        telegram_handler,
        log_record_factory,
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

        responses = telegram_handler.emit(log_record)
        assert isinstance(responses, dict)

        for value in responses.values():
            assert isinstance(value, requests.Response) or value is None
