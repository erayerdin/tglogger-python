import logging
import os
import tempfile
import traceback
import typing
import zipfile

import requests

_BASE_URL = "https://api.telegram.org/bot{token}/{method}"


# def _send_stack_trace(
#     generic_info_response: requests.Response,
#     handler: logging.Handler,
#     record: logging.LogRecord,
#     chat_id: int,
# ) -> typing.Union[None, requests.Response]:
#     """
#     Send stack trace for log in Telegram.
#     """
#     if record.exc_info is None or record.exc_info == (None, None, None):
#         return None
#
#     stack_trace_file = tempfile.NamedTemporaryFile(
#         mode="w+b", prefix="stacktrace-{}".format(uuid.uuid1()), suffix=".txt"
#     )
#
#     tback = record.exc_info[1].__traceback__
#     tback_data = traceback.format_tb(tback)
#
#     for data in tback_data:
#         stack_trace_file.write(data.encode())
#
#     stack_trace_file.seek(0)
#
#     message = textwrap.dedent(
#         """
#     #{uuid_hex}
#     Exception raised by **{exception_class_name}**.
#     """
#     ).strip()
#
#     reply_id = generic_info_response.json()["result"]["message_id"]
#     response = requests.post(
#         url=_BASE_URL.format(token=handler.bot_token, method="sendDocument"),
#         data={
#             "chat_id": chat_id,
#             "caption": message.format(
#                 uuid_hex=record.uuid.hex,
#                 exception_class_name=record.exc_info[0].__name__,
#             ),
#             "parse_mode": "markdown",
#             "reply_to_message_id": reply_id,
#         },
#         files={"document": stack_trace_file},
#     )
#
#     stack_trace_file.close()
#     return response


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


def build_zip_file(
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
    meta_zip_file = build_zip_file(record, stack_trace_file)
    stack_trace_file.close()
    return meta_zip_file


def send_log(
    handler: logging.Handler, record: logging.LogRecord, chat_id: int
) -> requests.Response:
    """
    Sends log to Telegram chat.
    """

    data = {"chat_id": chat_id, "parse_mode": "markdown"}

    if record.exc_info is None:
        method = "sendMessage"
        data["text"] = handler.format(record)
        meta_file = None
        files = None
    else:
        method = "sendDocument"
        data["caption"] = handler.format(record)
        meta_file = _build_meta_file(record)
        meta_file.seek(0)
        files = {"document": meta_file}

    response = requests.post(
        url=_BASE_URL.format(token=handler.bot_token, method=method),
        data=data,
        files=files,
    )

    if meta_file is not None:
        meta_file.close()

    return response
