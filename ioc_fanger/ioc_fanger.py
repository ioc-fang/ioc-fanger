"""Fang and defang indicators of compromise."""

import click

from ioc_fanger.regexes_defang import _at_re, _dot_re
from ioc_fanger.regexes_fang import fang_mappings

_BRACKET_CHARS = "[](){}"


def fang(text: str, debug: bool = False) -> str:
    """Fang the indicators in the given text."""
    fanged_text = text
    has_brackets = any(c in fanged_text for c in _BRACKET_CHARS)

    if debug:
        print(f"Starting text: {fanged_text}")
        print("-----")

    for mapping in fang_mappings:
        if mapping.get("requires_brackets") and not has_brackets:
            continue

        if debug:
            print(f"Mapping: {mapping}")

        fanged_text = mapping["find"].sub(mapping["replace"], fanged_text)

        if debug:
            print(f"Text after mapping: {fanged_text}")
            print("-----")

    return fanged_text


@click.command()
@click.argument("text", required=False)
def cli_fang(text: str | None) -> None:
    """CLI interface for fanging indicators."""
    if text:
        fanged_text = fang(text)
        print(fanged_text)
        return

    stdin_text = click.get_text_stream("stdin")
    if stdin_text:
        for line in stdin_text:
            fanged_text = fang(line.rstrip("\n"))
            print(fanged_text)


def defang(text: str) -> str:
    """Defang the indicators in the given text."""
    defanged_text = _dot_re.sub("[.]", text)
    defanged_text = defanged_text.replace("https:", "hXXps:").replace("http:", "hXXp:")
    defanged_text = _at_re.sub("(at)", defanged_text)
    return defanged_text


@click.command()
@click.argument("text", required=False)
def cli_defang(text: str | None) -> None:
    """CLI interface for defanging indicators."""
    if text:
        defanged_text = defang(text)
        print(defanged_text)
        return

    stdin_text = click.get_text_stream("stdin")
    if stdin_text:
        for line in stdin_text:
            defanged_text = defang(line.rstrip("\n"))
            print(defanged_text)
