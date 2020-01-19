"""
This module contains a formatter for logging with Telegram.
"""

import logging
import os
from textwrap import dedent


def _reformat_markdown_safe(text: str) -> str:
    """
    Sanitizes the provided text of special markdown characters. `_` and `*` characters
    are sanitized.
    """

    text = text.replace("_", "\_")  # noqa
    text = text.replace("*", "\*")  # noqa
    return text


class TelegramFormatter(logging.Formatter):
    """
    A `logging.Formatter` implementation for sending log records with Telegram.
    """

    _TEMPLATE = dedent(
        """
    #tglogger
    #{uuid_hex}
    *Logger Name:* {logger_name}
    *System Date:* {system_date} ({zone})
    *Level:* #{level_name}
    *Path and Line:* _{path}_:{lineno}
    *Function/Method:* _{func_name}_
    *Thread ID and Name:* \[{thread_id}] {thread_name}
    *Process ID and Name:* \[{process_id}] {process_name}

    *Message*
    {message}
    """
    ).strip()  # noqa

    def format(self, record: logging.LogRecord):
        data = dict()

        data["uuid_hex"] = record.uuid.hex
        data["logger_name"] = record.name

        if os.environ.get("DJANGO_SETTINGS_MODULE", None):
            from django.utils import timezone
            from django.conf import settings

            tz = getattr(settings, "TIME_ZONE", "No Timezone")
            use_tz = getattr(settings, "USE_TZ", False)

            if not use_tz:
                tz = "No Timezone"

            data["system_date"] = timezone.now()
            data["zone"] = tz
        else:
            from datetime import datetime

            data["system_date"] = datetime.now()
            data["zone"] = "No Timezone"

        data["level_name"] = record.levelname.lower()
        data["path"] = _reformat_markdown_safe(record.pathname)
        data["lineno"] = record.lineno
        data["func_name"] = _reformat_markdown_safe(record.funcName)
        data["thread_id"] = record.thread
        data["thread_name"] = record.threadName

        data["process_id"] = record.process
        data["process_name"] = record.processName
        data["message"] = record.getMessage()

        return self._TEMPLATE.format_map(data)
