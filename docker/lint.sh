#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort ioc_fanger/ tests/

black ioc_fanger/ tests/

mypy ioc_fanger/ tests/

pylint --fail-under 9 ioc_fanger/*.py

flake8 ioc_fanger/

# we run black again at the end to undo any odd changes made by any of the linters above
black ioc_fanger/ tests/
