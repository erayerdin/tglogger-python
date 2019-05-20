# Limitations

`tglogger` is not meant to be a replacement for cloud logging services such as Sentry
or Rollbar and there are clear limitations on what you can do with `tglogger`. In this
section, it is aimed to be mention these limitations.

## Cloud Logging Services

Cloud logging services provide you

 - the live log captures
 - the history of logging
 - stats and charts of log records
 - email notifications

and many more. That is why the services you get from these are going to be far superior
than using `tglogger` alone. `tglogger` is meant to be a helper for collaborative and
small-scoped projects and it currently helps you to only;

 - capture the live logging records and
 - the history of logging

with some limitations from both the side of Telegram and this library's way of doing things.

Also consider that cloud logging services already provide free services with their limitations.

## Telegram Bot Request Throttle

[According to Telegram's FAQ on bots](https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this),
Telegram limits the requests made to the server with the amounts below:

 - **30 messages** to *same individual* per **one second or so**
 - **1 message** to *different individuals* per **one second or so**
 - **20 messages** to *same group* per **one minute**

The table below can give you idea in what amount you can send logs *theoretically*:

| | per minute | per hour | per day | per week | per month (30 days) |
|---|---|---|---|---|---|
| **individual** (only log)       | 1.800 | 108.000 | 2.592.000 | 18.144.000 | 544.320.000 |
| **individual** (log+stacktrace) | 900 | 54.000 | 1.296.000 | 9.072.000 | 272.160.000 |
| **group** (only log)            | 20 | 1.200 | 28.800 | 201.600 | 6.048.000 |
| **group** (log+stacktrace)      | 10 | 600 | 14.400 | 100.800 | 3.024.000 |
