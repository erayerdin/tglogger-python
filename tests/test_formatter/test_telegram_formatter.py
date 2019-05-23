import re


class TestTelegramFormatter:
    def test_banner_hashtag(self, formatter_message):
        assert "#tglogger" in formatter_message

    def test_uuid(self, formatter_message):
        assert re.search("#[a-z0-9]{32}\n", formatter_message)

    def test_logger_name(self, formatter_message):
        assert "*Logger Name:* example.logger" in formatter_message

    def test_system_date(self, formatter_message):
        assert re.search(r"\*System Date:\* .*\n", formatter_message)

    def test_level(self, formatter_message):
        assert "*Level:* #error" in formatter_message

    def test_path_and_line(self, formatter_message):
        assert "*Path and Line:* _/foo/bar/baz.py_:1" in formatter_message

    def test_function_or_method(self, formatter_message):
        assert "*Function/Method:* _foo\_bar\_baz_" in formatter_message

    def test_thread(self, formatter_message):
        assert re.search(
            "\*Thread ID and Name:\* \\\[[0-9]+\] .*\n", formatter_message
        )

    def test_process(self, formatter_message):
        assert re.search(
            "\*Process ID and Name:\* \\\[[0-9]+\] .*\n", formatter_message
        )

    def test_message(self, formatter_message):
        assert "*Message*\n" in formatter_message
