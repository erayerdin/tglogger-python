import re


def test_message_banner_hashtag(formatter_message):
    assert "#tglogger" in formatter_message


def test_message_uuid(formatter_message):
    assert re.search("#[a-z0-9]{32}\n", formatter_message)


def test_message_logger_name(formatter_message):
    assert "*Logger Name:* example.logger" in formatter_message


def test_message_system_date(formatter_message):
    assert re.search(r"\*System Date:\* .*\n", formatter_message)


def test_message_level(formatter_message):
    assert "*Level:* #error" in formatter_message


def test_message_path_and_line(formatter_message):
    assert "*Path and Line:* _/foo/bar/baz.py_:1" in formatter_message


def test_message_function_or_method(formatter_message):
    assert r"*Function/Method:* _foo\_bar\_baz_" in formatter_message


def test_message_thread(formatter_message):
    assert re.search(
        r"\*Thread ID and Name:\* \\\[[0-9]+\] .*\n", formatter_message
    )


def test_message_process(formatter_message):
    assert re.search(
        r"\*Process ID and Name:\* \\\[[0-9]+\] .*\n", formatter_message
    )


def test_message_message(formatter_message):
    assert "*Message*\n" in formatter_message
