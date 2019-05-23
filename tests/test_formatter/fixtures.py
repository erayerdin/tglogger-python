import pytest


@pytest.fixture(scope="module")
def formatter_message(log_record_factory, telegram_formatter):
    log_record = log_record_factory()
    return telegram_formatter.format(log_record)
