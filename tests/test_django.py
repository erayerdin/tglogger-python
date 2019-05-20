import os
import re

import pytest

pytestmark = pytest.mark.skipIf(
    os.environ.get("DJANGO_SETTINGS_MODULE", None) is None,
    reason="Django does not exist in the environment.",
)


@pytest.fixture
def formatter_message_factory(
    settings, log_record_factory, telegram_formatter
):
    def factory(USE_TZ=True, TIME_ZONE="Europe/Istanbul"):
        settings.USE_TZ = USE_TZ
        settings.TIME_ZONE = TIME_ZONE

        log_record = log_record_factory()
        message = telegram_formatter.format(log_record)
        return message

    return factory


class TestTelegramFormatterDjango:
    def test_system_date_use_tz(self, formatter_message_factory, settings):
        assert (
            re.search(
                r"\*System Date:\* .* \(Europe/Istanbul\)\n",
                formatter_message_factory(),
            )
            is not None
        )

    def test_system_date_not_use_tz(self, formatter_message_factory, settings):
        assert (
            re.search(
                r"\*System Date:\* .* \(No Timezone\)\n",
                formatter_message_factory(USE_TZ=False),
            )
            is not None
        )

    def test_system_date_time_zone(self, formatter_message_factory, settings):
        assert (
            re.search(
                r"\*System Date:\* .* \(UTC\)\n",
                formatter_message_factory(TIME_ZONE="UTC"),
            )
            is not None
        )
