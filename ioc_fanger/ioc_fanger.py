"""Fang and defang indicators of compromise."""

import json
import os
import re

import click

FANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./fang.json"))
DEFANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./defang.json"))


def _get_data_from_file(file_path: str):
    """Get data from the given file path."""
    with open(file_path, 'r') as f:
        return json.loads(f.read())


# get the mappings to fang/defang indicators of compromise
fanging_mappings = _get_data_from_file(FANG_DATA_PATH)
defanging_mappings = _get_data_from_file(DEFANG_DATA_PATH)


def _fang_text(mapping, text: str) -> str:
    find_value = mapping['find']
    if not mapping.get('regex'):
        find_value = re.escape(find_value)

    flags = 0

    if not mapping.get('case_sensitive'):
        flags = re.IGNORECASE

    fanged_text = re.sub(find_value, mapping['replace'], text, flags=flags)

    return fanged_text


def fang(text: str, debug=False):
    """Fang the indicators in the given text."""
    fanged_text = text
    if debug:
        print('Starting text: {}'.format(fanged_text))
        print('-----')

    for mapping in fanging_mappings:
        if debug:
            print('Mapping: {}'.format(mapping))

        fanged_text = _fang_text(mapping, fanged_text)

        if debug:
            print('Text after mapping: {}'.format(fanged_text))
            print('-----')

    return fanged_text


@click.command()
@click.argument('text', required=False)
def cli_fang(text):
    """CLI interface for fanging indicators."""
    stdin_text = click.get_text_stream('stdin')

    if text:
        fanged_text = fang(text)
        print(fanged_text)
    elif stdin_text:
        for line in stdin_text:
            fanged_text = fang(line.rstrip('\n'))
            print(fanged_text)


def defang(text):
    """Defang the indicators in the given text."""
    defanged_text = text

    for mapping in defanging_mappings:

        def _replace(matches):
            """Replace matches.groups(1) with mapping['replace']."""
            try:
                return matches.group(0).replace(matches.group(1), mapping['replace'])
            except IndexError:
                return matches.group(0).replace(mapping['find'], mapping['replace'])

        defanged_text = re.sub(mapping['find'], _replace, defanged_text)

    return defanged_text


@click.command()
@click.argument('text', required=False)
def cli_defang(text):
    """CLI interface for defanging indicators."""
    stdin_text = click.get_text_stream('stdin')

    if text:
        defanged_text = defang(text)
        print(defanged_text)
    elif stdin_text:
        for line in stdin_text:
            defanged_text = defang(line.rstrip('\n'))
            print(defanged_text)
