# tglogger

[![PyPI](https://img.shields.io/pypi/v/tglogger.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI](https://img.shields.io/pypi/status/tglogger.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI](https://img.shields.io/pypi/dm/tglogger.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI](https://img.shields.io/pypi/pyversions/tglogger.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI](https://img.shields.io/pypi/l/tglogger.svg?style=flat-square)][pypi_url]
[![](https://img.shields.io/readthedocs/tglogger.svg?style=flat-square)](https://tglogger.readthedocs.io/en/latest/)
[![Telegram](https://img.shields.io/badge/telegram-%40erayerdin-%2332afed.svg?style=flat-square&logo=telegram&logoColor=white)](https://t.me/erayerdin)
[![Code Style](https://img.shields.io/badge/style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

![](resources/recording.gif)

`tglogger` contains utilities to build and redirect logs to
Telegram chat via a bot.

[pypi_url]: https://pypi.org/project/tglogger/

|              | Build | Coverage |
|--------------|-------|----------|
| **Master**   | [![Travis (.com) master](https://img.shields.io/travis/com/erayerdin/tglogger/master.svg?style=flat-square&logo=travis&logoColor=white)][travis_url] | [![](https://img.shields.io/coveralls/github/erayerdin/tglogger/master.svg?logo=star&logoColor=white&style=flat-square)][coveralls_url] |
| **Development** | [![Travis (.com) development](https://img.shields.io/travis/com/erayerdin/tglogger/development.svg?style=flat-square&logo=travis&logoColor=white)][travis_url] | [![](https://img.shields.io/coveralls/github/erayerdin/tglogger/development.svg?logo=star&logoColor=white&style=flat-square)][coveralls_url] |

[travis_url]: https://travis-ci.com/erayerdin/tglogger
[coveralls_url]: https://coveralls.io/github/erayerdin/tglogger

## Installing

Install via `pip`:

```bash
pip install tglogger
```

## Example

`tglogger` contains a formatter which formats log records for
Telegram chats and a handler which sends log records to a Telegram
chat.

Assuming you have a logger instance:

```python
logger = logging.getLogger(__name__)
```

You need to have an instance of `TelegramHandler` handler
`TelegramFormatter`.

```python
from tglogger import TelegramHandler, TelegramFormatter

handler = TelegramHandler(bot_token="foo", receiver="bar")
# you can also set TELEGRAM_BOT_TOKEN and TELEGRAM_RECEIVER
# environment variables so as not to pass these on initialization

formatter = TelegramFormatter() # initialize formatter
handler.setFormatter(formatter)  # inject formatter into handler

logger.addHandler(handler)  # inject handler into logger
```

And now your log records that has level above `ERROR` will be sent
to the chat you have defined with `receiver` by the bot that you
have defined by `bot_token`.

```python
logger.error("foo")  # you will receiver message by your bot
```

## Documentation

Documentation has more  information about how to use `tglogger`.
Refer to the
[documentation](https://tglogger.readthedocs.io/en/latest/).
