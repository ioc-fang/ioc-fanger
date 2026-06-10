"""Fang and defang indicators of compromise."""

import logging

import click

from ioc_fanger.regexes_defang import _at_re, _dot_re
from ioc_fanger.regexes_fang import fang_mappings

logger = logging.getLogger(__name__)

_BRACKET_CHARS = "[](){}"


def fang(text: str, debug: bool = False) -> str:
    """Fang the indicators in the given text."""
    fanged_text = text
    has_brackets = any(c in fanged_text for c in _BRACKET_CHARS)
    # Lower-cased copy of the text, used by case-insensitive `requires_any`
    # gates. Computed lazily (and refreshed) the first time a gate needs it so
    # text that triggers no such gate never pays for the `.lower()`.
    lowered_text: str | None = None

    if debug:
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            logger.addHandler(logging.StreamHandler())

    logger.debug("Starting text: %s", fanged_text)
    logger.debug("-----")

    for mapping in fang_mappings:
        logger.debug("Mapping: %s", mapping)

        if mapping.get("requires_brackets") and not has_brackets:
            logger.debug("No brackets found - skipping")
            continue

        # Skip a mapping whose required literal substrings are all absent: the
        # substitution could not match, so running it would be a no-op (same
        # idea as `requires_brackets`). Case-sensitive gates match the text
        # verbatim; case-insensitive gates match a lower-cased copy.
        requires_any = mapping.get("requires_any")
        if requires_any is not None:
            if mapping.get("case_sensitive"):
                haystack = fanged_text
            else:
                if lowered_text is None:
                    lowered_text = fanged_text.lower()
                haystack = lowered_text
            if not any(literal in haystack for literal in requires_any):
                logger.debug("No required literal found - skipping")
                continue

        new_text = mapping["find"].sub(mapping["replace"], fanged_text)
        if new_text != fanged_text:
            # A substitution occurred, so any cached lower-cased copy is stale.
            lowered_text = None
        fanged_text = new_text

        logger.debug("Text after mapping: %s", fanged_text)
        logger.debug("-----")

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
