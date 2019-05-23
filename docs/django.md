# Django Integration

You can integrate tglogger with Django as well so as to get live logging
records. See the example `LOGGING` settings below:

```python
LOGGING = {
    # ...
    "formatters": {
        # ...
        "telegram_formatter": {
            "()": "tglogger.formatter.TelegramFormatter"
        },
        # ...
    },
    # ...
    "handlers": {
        # ...
        "telegram_handler": {
            "class": "tglogger.handler.TelegramHandler",
            "formatter": "telegram_formatter",
            "bot_token": "BOT_TOKEN",  # replace it with your token
            "receiver": "CHAT_ID",  # chat id to send message to
        },
        # ...
    },
    # ...
}
```

!!! tip
    Instead of explicitly defining `bot_token` and `receiver` in the
    configuration, you can set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_RECEIVER`
    environment variables.

The default logging level for `TelegramHandler` is `ERROR`, you can change
this behavior by simply passing `level` to the handler in the `LOGGING`
*dictConfig*.

```python
# assuming you have set TELEGRAM_BOT_TOKEN and TELEGRAM_RECEIVER environment variables
"handlers": {
    "telegram_handler": {
        "class": "tglogger.formatter.TelegramHandler",
        "formatter": "telegram_formatter",
        "level", "INFO",
    },
},
```
