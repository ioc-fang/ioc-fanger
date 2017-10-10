#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ioc_fanger_cli
----------------------------------

Tests for `ioc_fanger` cli.
"""

import os

import docopt
import pytest

from ioc_fanger import cli


@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    # TODO: Add command line arguments here (see: https://github.com/docopt/docopt#api)

    return args


def test_command_line_interface(command_line_args):
    """Test the command line usage of this project."""
    # TODO: Add more robust testing here
    with pytest.raises(docopt.DocoptExit) as exc_info:
        cli.main()

    # get the error message
    error_message = exc_info.value
    # make sure the error message contains the expected usage output
    assert "Usage:" in str(error_message)
