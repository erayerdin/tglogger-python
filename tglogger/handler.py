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


class TelegramHandler(logging.Handler):
    def __init__(
        self,
        level=logging.ERROR,
        bot_token: str = os.environ["TELEGRAM_BOT_TOKEN"],
        receiver: str = os.environ["TELEGRAM_RECEIVER"],
    ):
        self.bot_token = bot_token
        self.receiver = receiver
        super().__init__(level)

    def emit(self, record):
        return request.send_log(self, record, self.receiver)
