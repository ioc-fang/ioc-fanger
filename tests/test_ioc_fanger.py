#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ioc_fanger
----------------------------------

Tests for `ioc_fanger` module.
"""

import os

import pytest

from ioc_fanger import ioc_fanger


@pytest.fixture
def defanged_text():
    """Function to simulate command line arguments using docopt."""
    return "hxxp://test[.]com 1[.]2[.]3[.]4 bob[@]example.com"


@pytest.fixture
def fanged_text():
    """Function to simulate command line arguments using docopt."""
    return "http://test.com 1.2.3.4 bob@example.com"


def test_fanging(defanged_text, fanged_text):
    """Test fanging."""
    test_fanged_text = ioc_fanger.fang(defanged_text)

    assert test_fanged_text == fanged_text


def test_defanging(fanged_text):
    """Test defanging."""
    defanged_text = ioc_fanger.defang(fanged_text)

    assert "hXXp://test[.]com" in defanged_text
    assert "1[.]2.3[.]4" in defanged_text
    assert "bob@example[.]com" in defanged_text
