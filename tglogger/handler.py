import logging
import os

from tglogger import request


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
