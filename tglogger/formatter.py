# todo - 2 class doc

import logging

MESSAGE_LINE_TEMPLATES = (
    "#tglogger",
    "*Logger Name:* {logger_name}",
    "*System Date:* {system_date}",
    "*Level:* #{level_name}",
    "*Path and Line:* _{path}_:{lineno}",
    "*Function/Method:* _{func_name}_",
    "*Thread ID and Name:* \[{thread_id}] {thread_name}",
    "*Process ID and Name:* \[{process_id}] {process_name}",
    "\n*Message*\n{message}\n",
)


def reformat_markdown_safe(text: str) -> str:
    # todo - 2 function doc

    text = text.replace("_", "\_")
    text = text.replace("*", "\*")
    return text


class TelegramFormatter(logging.Formatter):
    # todo 3 - class doc

    def format(self, record: logging.LogRecord):
        message_lines = [MESSAGE_LINE_TEMPLATES[0]]

        logger_name = record.name
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[1].format(logger_name=logger_name)
        )

        try:
            from django import timezone as datetime
            from django import settings

            tz = getattr(settings, "TIME_ZONE", "No Timezone")

            system_date = "{now} ({zone})".format(now=datetime.now(), zone=tz)
        except ImportError:
            from datetime import datetime

            system_date = datetime.now()
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[2].format(system_date=system_date)
        )

        level_name = record.levelname.lower()
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[3].format(level_name=level_name)
        )

        path = reformat_markdown_safe(record.pathname)
        lineno = record.lineno
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[4].format(path=path, lineno=lineno)
        )

        func_name = reformat_markdown_safe(record.funcName)
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[5].format(func_name=func_name)
        )

        thread_id = record.thread
        thread_name = record.threadName
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[6].format(
                thread_id=thread_id, thread_name=thread_name
            )
        )

        process_id = record.process
        process_name = record.processName
        message_lines.append(
            MESSAGE_LINE_TEMPLATES[7].format(
                process_id=process_id, process_name=process_name
            )
        )

        message = record.getMessage()
        message_lines.append(MESSAGE_LINE_TEMPLATES[8].format(message=message))

        return "\n".join(message_lines)
