"""Fang and defang indicators of compromise."""

import logging

import click

from ioc_fanger.regexes_defang import defang_mappings
from ioc_fanger.regexes_fang import fang_mappings

logger = logging.getLogger(__name__)


def fang(text: str, debug=False):
    """Fang the indicators in the given text."""
    fanged_text = text

    if debug:
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            logger.addHandler(logging.StreamHandler())

    logger.debug("Starting text: %s", fanged_text)
    logger.debug("-----")

    for mapping in fang_mappings:
        logger.debug("Mapping: %s", mapping)

        fanged_text = mapping["find"].sub(mapping["replace"], fanged_text)

        logger.debug("Text after mapping: %s", fanged_text)
        logger.debug("-----")

    return fanged_text


@click.command()
@click.argument("text", required=False)
def cli_fang(text):
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


def defang(text):
    """Defang the indicators in the given text."""
    defanged_text = text

    for mapping in defang_mappings:
        defanged_text = mapping["find"].sub(mapping["replace"], defanged_text)

    return defanged_text


@click.command()
@click.argument("text", required=False)
def cli_defang(text):
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
