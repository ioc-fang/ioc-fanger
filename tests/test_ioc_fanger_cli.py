#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ioc_fanger
----------------------------------

Tests for `ioc_fanger` module.
"""

import pytest
from click.testing import CliRunner

from ioc_fanger import ioc_fanger
from .test_ioc_fanger import defanged_text, fanged_text


def test_fang_cli(defanged_text, fanged_text):
    runner = CliRunner()
    result = runner.invoke(ioc_fanger.cli_fang, [defanged_text])
    assert result.exit_code == 0
    assert result.output.strip() == fanged_text


def test_defang_cli(defanged_text, fanged_text):
    runner = CliRunner()
    result = runner.invoke(ioc_fanger.cli_defang, [fanged_text])
    assert result.exit_code == 0
    assert "hXXp://example[.]com" in result.output
    assert "1[.]2.3[.]4" in result.output
    assert "bob(at)example[.]com" in result.output
