#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fang and defang indicators of compromise."""

import json
import os
import re

FANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./fang.json"))
DEFANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./defang.json"))


# The code below is legacy code that I will likely remove in the future
# import requests
# DEFANG_DATA_URL = "https://ioc-fang.github.io/datasets/defang.json"
# FANG_DATA_URL = "https://ioc-fang.github.io/datasets/fang.json"
# def _get_data_from_url(url):
#     """Get data from the given url."""
#     response = requests.get(url)

#     if response.ok:
#         return json.loads(response.text)


def _get_data_from_file(file_path):
    """Get data from the given file path."""
    with open(file_path, 'r') as f:
        return json.loads(f.read())


# get the mappings to fang/defang indicators of compromise
fanging_mappings = _get_data_from_file(FANG_DATA_PATH)
defanging_mappings = _get_data_from_file(DEFANG_DATA_PATH)


def fang(text):
    """Fang the indicators in the given text."""
    fanged_text = text

    for mapping in fanging_mappings:
        fanged_text = re.sub(re.escape(mapping['find']), mapping['replace'],
                             fanged_text, flags=re.IGNORECASE)

    return fanged_text


def defang(text):
    """Defang the indicators in the given text."""
    defanged_text = text

    for mapping in defanging_mappings:
        def _replace(matches):
            """Replace matches.groups(1) with mapping['replace']."""
            try:
                return matches.group(0).replace(matches.group(1),
                                                mapping['replace'])
            except IndexError as e:
                return matches.group(0).replace(mapping['find'], mapping['replace'])

        defanged_text = re.sub(mapping['find'], _replace,
                               defanged_text)

    return defanged_text
