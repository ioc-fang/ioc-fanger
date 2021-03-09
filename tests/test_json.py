"""Make sure data files are in proper json format."""

import json
import os


def _read_file(file_path):
    """."""
    with open(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../ioc_fanger/{}".format(file_path))),
        "r",
    ) as f:
        json.loads(f.read())


def test_fanging_dataset():
    """Make sure fang.json is in proper json."""
    _read_file("fang.json")


def test_defanging_dataset():
    """Make sure defang.json is in proper json."""
    _read_file("defang.json")
