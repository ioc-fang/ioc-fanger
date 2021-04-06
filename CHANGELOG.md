# Changelog

We will document all notable changes to this project in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## Unreleased

## [3.2.1] - 2021.04.06

### Fixed

- Fixing lint errors
- Improving handling of "http" surrounded by angle brackets ([#48](https://github.com/ioc-fang/ioc-fanger/issues/48))

## [3.2.0] - 2021.03.09

### Added

- [Benchmarks](https://github.com/ionelmc/pytest-benchmark) to tests ([#41](https://github.com/ioc-fang/ioc-fanger/issues/41))

### Changed

- Reverting to use regexes rather than grammars (for the sake of performance) ([#38](https://github.com/ioc-fang/ioc-fanger/issues/38))
