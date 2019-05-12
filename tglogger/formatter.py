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
    *System Date:* {system_date}
    *Level:* #{level_name}
    *Path and Line:* _{path}_:{lineno}
    *Function/Method:* _{func_name}_
    *Thread ID and Name:* \[{thread_id}] {thread_name}
    *Process ID and Name:* \[{process_id}] {process_name}

    *Message*
    {message}
    """
    )

    def format(self, record: logging.LogRecord):
        data = dict()

        data["logger_name"] = record.name

        try:
            from django import timezone as datetime
            from django import settings

            tz = getattr(settings, "TIME_ZONE", "No Timezone")

            data["system_date"] = "{now} ({zone})".format(
                now=datetime.now(), zone=tz
            )
        except ImportError:
            from datetime import datetime

            data["system_date"] = datetime.now()

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
