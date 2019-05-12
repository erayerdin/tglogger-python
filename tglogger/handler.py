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
        self.__bot_token = bot_token
        self.__receiver = receiver
        super().__init__(level)

    def emit(self, record):
        session = request.BotSession(token=self.__bot_token)
        req = request.SendMessageRequest(
            session, self.__receiver, self.format(record)
        )
        return session.send(req)
