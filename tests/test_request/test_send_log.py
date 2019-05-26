import tglogger.request


def test_rtype(send_log_response):
    assert isinstance(send_log_response, tglogger.request.requests.Response)


# Regular


def test_request_url(send_log_request):
    assert send_log_request.url.endswith("sendMessage")


def test_request_body_chat_id(send_log_request_body):
    assert send_log_request_body["chat_id"][0] == "1"


def test_request_body_parse_mode(send_log_request_body):
    assert send_log_request_body["parse_mode"][0] == "markdown"


def test_request_body_text(send_log_request_body):
    assert "text" in send_log_request_body


# Exception


def test_exception_request_url(send_log_exception_request):
    assert send_log_exception_request.url.endswith("sendDocument")


def test_exception_request_caption(send_log_exception_request_body):
    assert b'name="caption"' in send_log_exception_request_body


def test_exception_request_document(send_log_exception_request_body):
    assert b'name="document"' in send_log_exception_request_body
