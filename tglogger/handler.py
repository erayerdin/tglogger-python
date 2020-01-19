"""
This module contains a handler for Telegram.
"""

import logging
import os
import uuid

from tglogger import request

_old_factory = logging.getLogRecordFactory()


def _log_record_uuid(*args, **kwargs):
    record = _old_factory(*args, **kwargs)
    record.uuid = uuid.uuid4()
    return record


logging.setLogRecordFactory(_log_record_uuid)


class InvalidBotError(Exception):
    """
    This error is raised if the provided bot token is invalid.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TelegramHandler(logging.Handler):
    """
    A `logging.Handler` implementation for sending log records with Telegram.
    """

    def __init__(
        self,
        level=logging.ERROR,
        bot_token: str = os.environ["TELEGRAM_BOT_TOKEN"],
        receiver: str = os.environ["TELEGRAM_RECEIVER"],
        **kwargs
    ):
        self.bot_token = bot_token
        self.receiver = receiver
        super().__init__(level)

        if not kwargs.get("bypass_auth", False):
            self._authorize()

    def _authorize(self):
        url = request._BASE_URL.format(token=self.bot_token, method="getMe")
        response = request.requests.get(url)

        if not response.ok:
            raise InvalidBotError("No bot exists with provided token.")

    def emit(self, record):
        return request.send_log(self, record, self.receiver)
