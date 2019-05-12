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
        self._bot_token = bot_token
        self._receiver = receiver
        super().__init__(level)

    def emit(self, record):
        session = request.BotSession(token=self._bot_token)
        req = request.SendMessageRequest(
            session, self._receiver, self.format(record)
        )
        return session.send(req)
