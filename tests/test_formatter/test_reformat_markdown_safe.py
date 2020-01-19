from tglogger import formatter


def test_reformat_markdown_safe_underscore():
    example = "foo_bar_baz"
    reformatted = formatter.reformat_markdown_safe(example)
    assert reformatted == "foo\_bar\_baz"  # noqa


def test_reformat_markdown_safe_asterisk():
    example = "foo*bar*baz"
    reformatted = formatter.reformat_markdown_safe(example)
    assert reformatted == "foo\*bar\*baz"  # noqa
