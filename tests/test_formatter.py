import re

import pytest

from tglogger import formatter


class TestMessageLineTemplate:
    def test_is_list_or_tuple(self):
        assert isinstance(
            formatter.MESSAGE_LINE_TEMPLATES, list
        ) or isinstance(formatter.MESSAGE_LINE_TEMPLATES, tuple)

    def test_item_banner_hashtag(self):
        assert "#tglogger" in formatter.MESSAGE_LINE_TEMPLATES

    def test_item_logger_name(self):
        assert (
            "*Logger Name:* {logger_name}" in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_system_date(self):
        assert (
            "*System Date:* {system_date}" in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_level(self):
        assert "*Level:* #{level_name}" in formatter.MESSAGE_LINE_TEMPLATES

    def test_item_path_and_line(self):
        assert (
            "*Path and Line:* _{path}_:{lineno}"
            in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_function_or_method(self):
        assert (
            "*Function/Method:* _{func_name}_"
            in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_thread(self):
        assert (
            "*Thread ID and Name:* \[{thread_id}] {thread_name}"
            in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_process(self):
        assert (
            "*Process ID and Name:* \[{process_id}] {process_name}"
            in formatter.MESSAGE_LINE_TEMPLATES
        )

    def test_item_message(self):
        assert "\n*Message*\n{message}\n" in formatter.MESSAGE_LINE_TEMPLATES


class TestReformatMarkdownSafe:
    def test_replace_underscore(self):
        example = "foo_bar_baz"
        reformatted = formatter.reformat_markdown_safe(example)
        assert reformatted == "foo\_bar\_baz"

    def test_replace_asterisk(self):
        example = "foo*bar*baz"
        reformatted = formatter.reformat_markdown_safe(example)
        assert reformatted == "foo\*bar\*baz"


@pytest.fixture(scope="module")
def formatter_message(log_record_factory, telegram_formatter):
    log_record = log_record_factory()
    return telegram_formatter.format(log_record)


class TestTelegramFormatter:
    def test_banner_hashtag(self, formatter_message):
        assert "#tglogger" in formatter_message

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
