# todo - 2 class doc

import logging
from textwrap import dedent


def reformat_markdown_safe(text: str) -> str:
    # todo - 2 function doc

    text = text.replace("_", "\_")
    text = text.replace("*", "\*")
    return text


class TelegramFormatter(logging.Formatter):
    # todo 3 - class doc
    _TEMPLATE = dedent(
        """
    #tglogger
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
    ).strip()

    def format(self, record: logging.LogRecord):
        data = dict()

        data["logger_name"] = record.name

        try:
            from django.utils import timezone
            from django.conf import settings

            tz = getattr(settings, "TIME_ZONE", "No Timezone")
            use_tz = getattr(settings, "USE_TZ", False)

            if not use_tz:
                tz = "No Timezone"

            data["system_date"] = timezone.now()
            data["zone"] = tz
        except ImportError:
            from datetime import datetime

            data["system_date"] = datetime.now()
            data["zone"] = "No Timezone"

        data["level_name"] = record.levelname.lower()
        data["path"] = reformat_markdown_safe(record.pathname)
        data["lineno"] = record.lineno
        data["func_name"] = reformat_markdown_safe(record.funcName)
        data["thread_id"] = record.thread
        data["thread_name"] = record.threadName

        data["process_id"] = record.process
        data["process_name"] = record.processName
        data["message"] = record.getMessage()

        return self._TEMPLATE.format_map(data)
