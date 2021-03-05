"""Fang and defang indicators of compromise."""

import json
import os
import re

import click

from ioc_fanger import grammars

FANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./fang.json"))
DEFANG_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./defang.json"))


def _get_data_from_file(file_path):
    """Get data from the given file path."""
    with open(file_path, "r") as f:
        return json.loads(f.read())


# get the mappings to fang/defang indicators of compromise
fanging_mappings = _get_data_from_file(FANG_DATA_PATH)
defanging_mappings = _get_data_from_file(DEFANG_DATA_PATH)


def fang(text, debug=False):
    """Fang the indicators in the given text."""
    fanged_text = text

    if debug:
        print("Starting text: {}".format(fanged_text))
        print("-----")

    fanged_text = grammars.dot_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.at_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.more_at_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.colon_slash_slash_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.colon_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.odd_url_scheme_form.transformString(fanged_text)
    fanged_text = grammars.http_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.www_fanging_patterns.transformString(fanged_text)
    fanged_text = grammars.comma_fanging_patterns.transformString(fanged_text)

    for mapping in fanging_mappings:
        if debug:
            print("Mapping: {}".format(mapping))

        if mapping.get("regex"):
            find_value = mapping["find"]
        else:
            find_value = re.escape(mapping["find"])

        if mapping.get("case_sensitive"):
            fanged_text = re.sub(find_value, mapping["replace"], fanged_text)
        else:
            fanged_text = re.sub(find_value, mapping["replace"], fanged_text, flags=re.IGNORECASE)

        if debug:
            print("Text after mapping: {}".format(fanged_text))
            print("-----")

    return fanged_text


@click.command()
@click.argument("text", required=False)
def cli_fang(text):
    """CLI interface for fanging indicators."""
    stdin_text = click.get_text_stream("stdin")

    if text:
        fanged_text = fang(text)
        print(fanged_text)
    elif stdin_text:
        for line in stdin_text:
            fanged_text = fang(line.rstrip("\n"))
            print(fanged_text)
    else:
        # TODO: add some handling here
        pass


def defang(text):
    """Defang the indicators in the given text."""
    defanged_text = text

    for mapping in defanging_mappings:

        def _replace(matches):
            """Replace matches.groups(1) with mapping['replace']."""
            try:
                return matches.group(0).replace(matches.group(1), mapping["replace"])
            except IndexError:
                return matches.group(0).replace(mapping["find"], mapping["replace"])

        defanged_text = re.sub(mapping["find"], _replace, defanged_text)

    return defanged_text


@click.command()
@click.argument("text", required=False)
def cli_defang(text):
    """CLI interface for defanging indicators."""
    stdin_text = click.get_text_stream("stdin")

    if text:
        defanged_text = defang(text)
        print(defanged_text)
    elif stdin_text:
        for line in stdin_text:
            defanged_text = defang(line.rstrip("\n"))
            print(defanged_text)
    else:
        # TODO: add some handling here
        pass
