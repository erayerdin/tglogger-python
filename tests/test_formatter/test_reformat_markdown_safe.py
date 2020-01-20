from tglogger import formatter


def test__reformat_markdown_safe_underscore():
    example = "foo_bar_baz"
    reformatted = formatter._reformat_markdown_safe(example)
    assert reformatted == "foo\_bar\_baz"  # noqa


def test__reformat_markdown_safe_asterisk():
    example = "foo*bar*baz"
    reformatted = formatter._reformat_markdown_safe(example)
    assert reformatted == "foo\*bar\*baz"  # noqa
