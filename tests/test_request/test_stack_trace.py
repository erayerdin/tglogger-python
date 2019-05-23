import re


def test_request_body_chat_id(stack_trace_request_body):
    assert b'name="chat_id"' in stack_trace_request_body


def test_request_body_parse_mode(stack_trace_request_body):
    assert b'name="parse_mode"' in stack_trace_request_body


def test_request_body_caption(stack_trace_request_body):
    assert b'name="caption"' in stack_trace_request_body


def test_request_body_caption_content_uuid(stack_trace_request_body):
    assert re.search(b"#[a-z0-9]{32}\n", stack_trace_request_body)


def test_request_body_caption_content_exception(stack_trace_request_body):
    assert b"Exception raised by **Exception**" in stack_trace_request_body


def test_request_body_reply_to_message_id(stack_trace_request_body):
    assert b'name="reply_to_message_id"' in stack_trace_request_body


def test_request_body_document(stack_trace_request_body):
    assert b'name="document"' in stack_trace_request_body
