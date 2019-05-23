pytest_plugins = (
    # Generic
    "tests.fixtures.internal",
    "tests.fixtures.logging",
    "tests.fixtures.resource",
    #
    "tests.test_request.fixtures",  # request fixtures
    "tests.test_formatter.fixtures",  # formatter fixtures
)
