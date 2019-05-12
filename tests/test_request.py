import tglogger.request


class TestBotSession:
    def test_has_token(self, bot_session):
        assert hasattr(bot_session, "token")

    def test_has_base_url(self, bot_session):
        assert hasattr(bot_session, "base_url")


class TestBotRequest:
    def setup_method(self):
        self.session = tglogger.request.BotSession("0")
        self.request = tglogger.request.BotRequest(self.session, "getMe")

    def test_url(self, bot_session, bot_request_factory):
        bot_request = bot_request_factory("getMe")
        url = "{base_url}{method_name}".format(
            base_url=bot_session.base_url, method_name="getMe"
        )
        assert bot_request.url == url


class TestSendMessageRequest:
    def test_url(self, bot_send_message_request):
        assert bot_send_message_request.url[-11:] == "sendMessage"

    def test_request_body_chat_id(
        self, bot_send_message_request, request_body_factory
    ):
        request_body = request_body_factory(bot_send_message_request)
        assert request_body.get("chat_id") == 1

    def test_request_body_text(
        self, bot_send_message_request, request_body_factory
    ):
        request_body = request_body_factory(bot_send_message_request)
        assert request_body.get("text") == "foo"

    def test_request_body_parse_mode(
        self, bot_send_message_request, request_body_factory
    ):
        request_body = request_body_factory(bot_send_message_request)
        assert request_body.get("parse_mode") == "Markdown"
