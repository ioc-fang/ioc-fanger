#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fang and defang indicators of compromise."""

import json
import re

import requests

FANG_API = "https://ioc-fang.github.io/fanging-dataset/refang.json"
DEFANG_API = "https://ioc-fang.github.io/defanging-dataset/defang.json"


def _get_data(api_url):
    """."""
    response = requests.get(api_url)

    if response.ok:
        return json.loads(response.text)


# get the mappings to fang/defang indicators of compromise
fanging_mappings = _get_data(FANG_API)
defaning_mappings = _get_data(DEFANG_API)


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

    for mapping in defaning_mappings:
        matches = re.findall(mapping['find'], defanged_text)
        if len(matches) > 1:
            def _replace(matches):
                """Replace matches.groups(1) with mapping['replace']."""
                return matches.group(0).replace(matches.group(1),
                                                mapping['replace'])

            defanged_text = re.sub(mapping['find'], _replace,
                                   defanged_text)
        else:
            defanged_text = re.sub(mapping['find'], mapping['replace'],
                                   defanged_text)

    return defanged_text
