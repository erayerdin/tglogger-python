# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
 - `meta-*.zip` file to log message.

### Changed
 - Now stacktrace file is sent inside *meta* zip file that is attached to main
 log message.

### Removed
 - Feature of sending stacktrace file as a separate message.

## [v0.1.1a1] - 2019-05-24
### Added
 - `TelegramHandler` now validates bot on initialization

## [v0.1.0b5] - 2019-05-21
### Added
 - Added `uuid` to `TelegramFormatter` and `request`
 - Added `uuid` via `setLogRecordFactory`

## [v0.1.0b4] - 2019-05-20
### Added
 - Now if any exception occurs, it can be sent with stack trace as a file to
 a chat.

### Changed
 - Now tglogger checks `DJANGO_SETTINGS_MODULE` environment variable instead of
 the presence of `django`.

## [v0.1.0b2] - 2019-05-19
### Changed
 - Refactored `tglogger.request` module to use simple function called `send_log`

## [v0.1.0b1] - 2019-05-14
### Added
 - Explicit Django support

### Changed
 - Optimized Django parts

## [v0.1.0a3] - 2019-05-13
### Added
 - `_TEMPLATE` to `TelegramFormatter`

### Removed
 - `MESSAGE_LINE_TEMPLATE` from `tglogger.formatter`

## [v0.1.0a1] - 2019-05-12
### Added
 - `TelegramHandler`
 - `TelegramFormatter`
