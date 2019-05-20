import logging
import tempfile
import traceback
import typing
import uuid

import requests

_BASE_URL = "https://api.telegram.org/bot{token}/{method}"


def _send_stack_trace(
    generic_info_response: requests.Response,
    handler: logging.Handler,
    record: logging.LogRecord,
    chat_id: int,
) -> typing.Union[None, requests.Response]:
    """
    Send stack trace for log in Telegram.
    """
    if record.exc_info is None or record.exc_info == (None, None, None):
        return None

    stack_trace_file = tempfile.NamedTemporaryFile(
        mode="w+b", prefix="stacktrace-{}".format(uuid.uuid1()), suffix=".txt"
    )

    tback = record.exc_info[1].__traceback__
    tback_data = traceback.format_tb(tback)

    for data in tback_data:
        stack_trace_file.write(data.encode())

    stack_trace_file.seek(0)

    reply_id = generic_info_response.json()["result"]["message_id"]
    response = requests.post(
        url=_BASE_URL.format(token=handler.bot_token, method="sendDocument"),
        data={
            "chat_id": chat_id,
            "caption": "Exception raised by **{}**.".format(
                record.exc_info[0].__name__
            ),
            "parse_mode": "markdown",
            "reply_to_message_id": reply_id,
        },
        files={"document": stack_trace_file},
    )

    stack_trace_file.close()
    return response


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

    stack_trace_response = _send_stack_trace(
        generic_info_response, handler, record, chat_id
    )

    return {
        "generic_info_response": generic_info_response,
        "stack_trace_response": stack_trace_response,
        "django_settings_response": None,
    }
