import logging
import typing

import requests

from tglogger.resource import _build_meta_file

_BASE_URL = "https://api.telegram.org/bot{token}/{method}"


def send_log(
    handler: logging.Handler, record: logging.LogRecord, chat_id: int
) -> requests.Response:
    """
    Sends log to Telegram chat.
    """

    data = {"chat_id": chat_id, "parse_mode": "markdown"}

    if record.exc_info is None:
        method = "sendMessage"
        data["text"] = handler.format(record)
        meta_file = None
        files = None
    else:
        method = "sendDocument"
        data["caption"] = handler.format(record)
        meta_file = _build_meta_file(record)
        meta_file.seek(0)
        files = {"document": meta_file}

    response = requests.post(
        url=_BASE_URL.format(token=handler.bot_token, method=method),
        data=data,
        files=files,
    )

    if meta_file is not None:
        meta_file.close()

    return response
