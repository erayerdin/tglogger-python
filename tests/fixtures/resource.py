import pytest


@pytest.fixture
def read_test_resource(request):
    def factory(file_name: str, mode="r"):
        file = open("tests/resources/{}".format(file_name), mode)
        request.addfinalizer(lambda: file.close())
        return file

    return factory
