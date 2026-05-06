# Changelog

We will document all notable changes to this project in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [UNRELEASED]

### Added

- Python 3.10, 3.11, 3.12, 3.13, and 3.14 support
- macOS (`Darwin-CPython-3.14-64bit`) and Linux (`Linux-CPython-3.14-64bit`) benchmark baselines under `.benchmarks/`

### Changed

- Migrated from pip/setuptools to uv for dependency management and packaging
- Switched build backend from setuptools to hatchling
- Replaced flake8, black, isort, and pylint with ruff for linting and formatting
- Switched PyPI publishing to trusted publishing (OIDC) — no more username/password secrets
- Updated CI and docs to use uv throughout
- Python 3.14 is now the default for local development (Dockerfile, benchmark storage)

### Removed

- Support for Python 3.7, 3.8, and 3.9 (minimum is now 3.10)
- `setup.py`, `setup.cfg`, and `mypy.ini` (configuration consolidated into `pyproject.toml`)
- `bump2version` (versions are managed directly in `pyproject.toml` and `ioc_fanger/__init__.py`)
- Docker-based local development; `uv` is now the supported way to test/lint/develop. Docker is retained only to generate and compare a Linux benchmark baseline that matches CI.
- `requirements.txt` and `requirements_dev.txt` (use `uv sync --locked --group dev` to set up a dev environment)

### Fixed

- Constrained the comma-separated IP fang regex (`a,b,c,d`) to require each octet to be in the valid IPv4 range `0-255`, so strings like `999,999,999,999` no longer match the IPv4 fang pattern ([#121](https://github.com/ioc-fang/ioc-fanger/pull/121))

## [4.2.1] - 2022.09.27

### Fixed

- Fixed incorrect find regex producing overly broad fanging of any character preceeded with a `\` ([#99](https://github.com/ioc-fang/ioc-fanger/issues/99))

## [4.2.0] - 2022.09.17

### Changed

- (Internal) Moving regexes from json files to Python files for improved readability ([#50](https://github.com/ioc-fang/ioc-fanger/issues/50))

## [4.1.0] - 2022.09.13

### Changed

- Simplifying regexes which find surrounding brackets to only fang characters surrounded by brackets on both sides ([#85](https://github.com/ioc-fang/ioc-fanger/pull/85))
    - e.g. With previous versions of this library, this: `a.]b` was fanged as: `a.b`. Now, `a.]b` will not be changed when fanging.

## [4.0.0] - 2022.07.14

### Fixed

- Refined parsing so schemes like `ldap` are properly preserved
  - We have dropped support for fanging certain, uncommon fanging strategies like `http!://example.com/test.php`; if you are regularly seeing this fanging strategy used and would like this to be readded, please raise an issue

### Removed

- Support for Python < 3.7

## [3.4.1] - 2022.02.23

### Fixed

- IP address fanging so that we fang only comma separated numbers bordered by whitespace or the start/end of a line ([#71](https://github.com/ioc-fang/ioc-fanger/issues/61))

## [3.4.0] - 2022.02.04

### Removed

- Removed pyparsing as a requirement ([#61](https://github.com/ioc-fang/ioc-fanger/issues/61))

## [3.3.0] - 2021.04.17

### Added

- Adding fanging for `<.>` ([#52](https://github.com/ioc-fang/ioc-fanger/issues/52))

## [3.2.3] - 2021.04.09

### Fixed

- Limited replacement of characters between `http(s)` and `://` by changing `(https?)(?!s)\\S*?://` to `(https?)\\S{0,2}?://` ([#53](https://github.com/ioc-fang/ioc-fanger/issues/53))
- Not replacing `http://` or `https://` in URL paths/query strings ([#53](https://github.com/ioc-fang/ioc-fanger/issues/53))

## [3.2.2] - 2021.04.07

### Fixed

- Reduced false positives by not fanging periods and commas with spaces after them ([#47](https://github.com/ioc-fang/ioc-fanger/issues/47)) (e.g. previously `a. [b]` was fanged as `a.b]` - we've updated this to prevent false positives so that `a. [b]` is not fanged)

## [3.2.1] - 2021.04.06

### Fixed

- Fixing lint errors
- Improving handling of "http" surrounded by angle brackets ([#48](https://github.com/ioc-fang/ioc-fanger/issues/48))

## [3.2.0] - 2021.03.09

### Added

- [Benchmarks](https://github.com/ionelmc/pytest-benchmark) to tests ([#41](https://github.com/ioc-fang/ioc-fanger/issues/41))

### Changed

- Reverting to use regexes rather than grammars (for the sake of performance) ([#38](https://github.com/ioc-fang/ioc-fanger/issues/38))
