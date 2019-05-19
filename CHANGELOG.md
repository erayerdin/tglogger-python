# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
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
