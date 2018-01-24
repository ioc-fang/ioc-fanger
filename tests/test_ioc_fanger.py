#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ioc_fanger
----------------------------------

Tests for `ioc_fanger` module.
"""

import json
import os

import ioc_fanger
import pytest


@pytest.fixture
def defanged_text():
    """Function to simulate command line arguments using docopt."""
    return "example[.]com hxxp://example[.]com hXXp://example[.]com example.com http://example.com hxxp://example[.]com 1[.]2[.]3[.]4 bob[@]example[.]com mary[@]example.com carlos[at]example.com juanita(at)example.com http[:]//example.org https[:]//example.org hXxps[:]//example.org/test?target=bad[@]test.com"


@pytest.fixture
def fanged_text():
    """Function to simulate command line arguments using docopt."""
    return "example.com http://example.com http://example.com example.com http://example.com http://example.com 1.2.3.4 bob@example.com mary@example.com carlos@example.com juanita@example.com http://example.org https://example.org https://example.org/test?target=bad@test.com"


def test_fanging(defanged_text, fanged_text):
    """Test fanging."""
    test_fanged_text = ioc_fanger.fang(defanged_text)

    assert test_fanged_text == fanged_text


def test_defanging(fanged_text):
    """Test defanging."""
    defanged_text = ioc_fanger.defang(fanged_text)

    assert "hXXp://example[.]com" in defanged_text
    assert "1[.]2.3[.]4" in defanged_text
    assert "bob@example[.]com" in defanged_text


def _read_file(file_path):
    """."""
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ioc_fanger/{}".format(file_path))), 'r') as f:
        json.loads(f.read())


def test_fanging_dataset():
    """Make sure fang.json is in proper json."""
    _read_file('fang.json')


def test_defanging_dataset():
    """Make sure defang.json is in proper json."""
    _read_file('defang.json')
