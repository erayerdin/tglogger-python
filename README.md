# tglogger

[![PyPI - Version][version_badge_url]][pypi_url]
[![PyPI - Status][status_badge_url]][pypi_url]
[![PyPI - License][license_badge_url]](LICENSE.txt)
![PyPI - Python][python_badge_url]
![PyPI - Django][django_badge_url]
![Downloads - Month][dlmonth_badge_url]

![](resources/recording.gif)

`tglogger` contains utilities to build and redirect logs to Telegram chat via a bot.

 - It has a formatter for beautiful log messages in Telegram.
 - It tends to *tag* common logs so that you can easily filter out related log messages.
 - You can send logs to individuals, channels or groups.
 - It works with Django (See badges for supported versions).

<!-- Meta Links Start -->

[version_badge_url]: https://img.shields.io/pypi/v/tglogger?label=version&logoColor=white&style=flat-square
[status_badge_url]: https://img.shields.io/pypi/status/tglogger?style=flat-square
[license_badge_url]: https://img.shields.io/pypi/l/tglogger?style=flat-square
[python_badge_url]: https://img.shields.io/pypi/pyversions/tglogger?color=3572a2&label=%20&logo=python&logoColor=FECE3D&style=flat-square
[django_badge_url]: https://img.shields.io/pypi/djversions/tglogger?color=092e20&label=%20&logo=django&logoColor=white&style=flat-square
[dlmonth_badge_url]: https://img.shields.io/pypi/dm/tglogger?label=dl%2Fmonth&style=flat-square

[pypi_url]: https://pypi.org/project/tglogger/

<!-- Meta Links End -->

| | Build | Coverage |
|-|---|---|
| **master** | [![Linux - Master][linux_master_badge_url]][linux_master_url] | [![Coverage - Master][codecov_master_badge_url]][codecov_master_url] |
| **development** | [![Linux - Development][linux_development_badge_url]][linux_development_url] | [![Coverage - Development][codecov_development_badge_url]][codecov_development_url] |

<!-- Build Links Start -->

[linux_development_badge_url]: https://img.shields.io/github/workflow/status/erayerdin/tglogger/testing/development?logo=linux&logoColor=white&style=flat-square
[linux_master_badge_url]: https://img.shields.io/github/workflow/status/erayerdin/tglogger/testing/master?logo=linux&logoColor=white&style=flat-square

[codecov_development_badge_url]: https://img.shields.io/codecov/c/gh/erayerdin/tglogger/development?style=flat-square
[codecov_master_badge_url]: https://img.shields.io/codecov/c/gh/erayerdin/tglogger/master?style=flat-square

[linux_development_url]: https://github.com/erayerdin/tglogger/actions?query=workflow%3A%22Build+and+Distribute%22+branch%3Adevelopment
[linux_master_url]: https://github.com/erayerdin/tglogger/actions?query=workflow%3A%22Build+and+Distribute%22+branch%3Amaster

[codecov_development_url]: https://codecov.io/gh/erayerdin/tglogger/branch/development
[codecov_master_url]: https://codecov.io/gh/erayerdin/tglogger/branch/master

<!-- Build Links End -->

## Installing

Install via `pip`:

```bash
pip install tglogger
```

## Example

`tglogger` contains a formatter which formats log records for Telegram chats and a handler which sends log records to a Telegram chat.

Assuming you have a logger instance:

```python
logger = logging.getLogger(__name__)
```

You need to have an instance of `TelegramHandler` and `TelegramFormatter`.

```python
from tglogger import TelegramHandler, TelegramFormatter

handler = TelegramHandler(bot_token="foo", receiver="bar")
# you can also set TELEGRAM_BOT_TOKEN and TELEGRAM_RECEIVER
# environment variables so as not to pass these on initialization

formatter = TelegramFormatter() # initialize formatter
handler.setFormatter(formatter)  # inject formatter into handler

logger.addHandler(handler)  # inject handler into logger
```

And now your log records that has level above `ERROR` will be sent to the chat you have defined with `receiver` by the bot that you have defined by `bot_token`.

```python
logger.error("foo")  # you will receive a message by your bot
```

## Documentation

Documentation has more information about how to use `tglogger`. Refer to the [documentation](https://tglogger.readthedocs.io/en/latest/).
