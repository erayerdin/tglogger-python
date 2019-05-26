import logging
import os
import tempfile
import traceback
import typing
import zipfile


def _build_stack_trace_file(
    record: logging.LogRecord
) -> tempfile.NamedTemporaryFile:
    stack_trace_file = tempfile.NamedTemporaryFile(
        mode="w+b",
        prefix="stacktrace-{}".format(record.uuid.hex),
        suffix=".txt",
    )

    tback = record.exc_info[1].__traceback__
    tback_data = traceback.format_tb(tback)

    for data in tback_data:
        stack_trace_file.write(data.encode())

    return stack_trace_file


def _build_zip_file(
    record: logging.LogRecord, *files: typing.List[tempfile.NamedTemporaryFile]
) -> tempfile.NamedTemporaryFile:
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+b", prefix="meta-{}".format(record.uuid.hex), suffix=".zip"
    )
    zip_file = zipfile.ZipFile(temp_file, mode="w")

    for file in files:
        file.seek(0)
        zip_file.write(file.name, os.path.basename(file.name))

    zip_file.close()
    return temp_file


def _build_meta_file(record: logging.LogRecord) -> tempfile.NamedTemporaryFile:
    stack_trace_file = _build_stack_trace_file(record)
    meta_zip_file = _build_zip_file(record, stack_trace_file)
    stack_trace_file.close()
    return meta_zip_file
