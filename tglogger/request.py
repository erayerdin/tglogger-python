import logging
import typing

import requests

_BASE_URL = "https://api.telegram.org/bot{token}/{method}"


def send_log(
    handler: logging.Handler, record: logging.LogRecord, chat_id: int
) -> typing.Dict[str, requests.Response]:
    """
    Sends log to Telegram chat.
    """
    generic_info_response = requests.post(
        url=_BASE_URL.format(token=handler.bot_token, method="sendMessage"),
        data={
            "chat_id": chat_id,
            "text": handler.format(record),
            "parse_mode": "markdown",
        },
    )

    return {
        "generic_info_response": generic_info_response,
        "stack_trace_response": None,
        "django_settings_response": None,
    }
