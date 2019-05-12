import requests


class TestTelegramHandler:
    def test_emit_return_type(self, telegram_handler, log_record_factory):
        log_record = log_record_factory()
        assert isinstance(telegram_handler.emit(log_record), requests.Response)
