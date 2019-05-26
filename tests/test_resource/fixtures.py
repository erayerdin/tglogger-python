import zipfile

import pytest

import tglogger.resource


# build_zip_file
@pytest.fixture
def meta_archive(temp_file, exception_log_record):
    archive_file = tglogger.resource._build_zip_file(
        exception_log_record, temp_file
    )
    archive = zipfile.ZipFile(archive_file, mode="r")
    yield archive
    archive.close()


@pytest.fixture
def meta_first_file(meta_archive):
    first_file = meta_archive.open(meta_archive.namelist()[0])
    yield first_file
    first_file.close()
