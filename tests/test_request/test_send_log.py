import tglogger.request


def test_rtype(send_log_response):
    assert isinstance(send_log_response, tglogger.request.requests.Response)


def test_request_body_chat_id(send_log_request_body):
    assert send_log_request_body["chat_id"][0] == "1"


def test_request_body_parse_mode(send_log_request_body):
    assert send_log_request_body["parse_mode"][0] == "markdown"


def test_request_body_text(send_log_request_body):
    assert "text" in send_log_request_body
