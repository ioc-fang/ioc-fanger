import re
from typing import List

# NOTE: Throughout this file, any regex matching a space (e.g. ` *`) must be escaped (e.g. `\ *`) b/c...
# we are compiling in verbose mode (which removes unescaped whitespace)

# The type hint for fang_patterns is required to make mypy happy...
# (to prevent "Unsupported right operand type for in ("object")")
fang_patterns: List = [
    {
        # "[://]" -> "://"
        "find": r"(\[:\/\/\])",
        "replace": "://",
    },
    {
        # Fang a period or comma surrounded by any kind of bracket
        # We don't allow spaces after the "." so we don't inadvertently fang valid sentences...
        # (e.g. we don't want to fang something like: "an example). [B]")
        "find": r"((\ *[\[\]\(\)\{\}]{1}\ *)[.,]([\[\]\(\)\{\}]{1}\ *))",
        "replace": ".",
    },
    {
        # Fang a colon surrounded by any kind of bracket
        "find": r"((\ *[\[\]\(\)\{\}]{1}\ *):(\ *[\[\]\(\)\{\}]{1}\ *))",
        "replace": ":",
    },
    {
        # Fang "DOT" surrounded by any kind of bracket
        "find": r"((\ *[\[\]\(\)\{\}]*\ *)DOT(\ *[\[\]\(\)\{\}]*\ *))",
        "replace": ".",
        "case_sensitive": True,
    },
    {
        # Fang any of the words in the middle of the regex preceded (and perhaps postceded) by any kind of bracket
        "find": r"((\ *[\[\]\(\)\{\}-]+\ *)(?:dot|punto|punkt)(\ *[\[\]\(\)\{\}-]*\ *))",
        "replace": ".",
    },
    {
        # Fang any of the words in the middle of the regex postceded (and perhaps preceded) by any kind of bracket
        "find": r"((\ *[\[\]\(\)\{\}-]*\ *)(?:dot|punto|punkt)(\ *[\[\]\(\)\{\}-]+\ *))",
        "replace": ".",
    },
    {
        # Fang any of the words in the middle of the regex preceded (and perhaps postceded) by any kind of bracket
        "find": r"((\ *[\[\]\(\{\}]+\ *)(?:@|(?:at)|(?:et)|(?:arroba))(\ *[\]\(\)\{\}]*\ *))",
        "replace": "@",
        "case_sensitive": True,
    },
    {
        # Fang any of the words in the middle of the regex postceded (and perhaps preceded) by any kind of bracket
        "find": r"((\ *[\[\]\(\)\{\}]*\ *)(?:@|(?:at)|(?:et)|(?:arroba))(\ *[\]\(\)\{\}]+\ *))",
        "replace": "@",
        "case_sensitive": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' preceded by a parenthesis/square brackets and possibly postceded by the same.
        "find": r"((\ *[\[\]\(\)\{\}]+\ *)(?:(?:AT)|(?:ET)|(?:ARROBA))(\ *[\[\]\(\)\{\}]*\ *))",
        "replace": "@",
        "case_sensitive": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' postceded by a parenthesis/square brackets and possibly preceded by the same.
        "find": r"((\ *[\[\]\(\)\{\}]*\ *)(?:(?:AT)|(?:ET)|(?:ARROBA))(\ *[\[\]\(\)\{\}]+\ *))",
        "replace": "@",
        "case_sensitive": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' preceded by a lower-cased character (and possibly spaces)
        "find": r"([a-z])\ *(?:AT|ET|ARROBA)\ *([a-z])",
        "replace": r"\1@\2",
        "case_sensitive": True,
    },
    {
        # Fang "www" surrounded by any kind of bracket
        "find": r"(([\[\]\(\)\{\}]{1}\ *)www(\ *[\[\]\(\)\{\}]{1}\ *))",
        "replace": "www",
    },
    {
        "find": r":\/\/\/+",
        "replace": "://",
    },
    {
        "find": r":\/\/ *",
        "replace": "://",
    },
    {
        "find": r": +\/\/",
        "replace": "://",
    },
    {
        # Fang "https?" preceded by a parenthesis/square brackets and possibly postceded by the same.
        # We don't fang closing brackets before "https?" b/c this not properly handle markdown links...
        # e.g. "[a](https://example.com)" would become "[ahttps://example.com" which is not ideal
        "find": r"(?:[\[\(\{]+\ *)htt(ps?)(?:\ *[\[\]\(\)\{\}]*\ *)",
        "replace": r"htt\1",
    },
    {
        # Fang "https?" postceded by a parenthesis/square brackets and possibly preceded by the same.
        "find": r"(?:[\[\]\(\)\{\}]*\ *)htt(ps?)(?:\ *[\[\]\(\)\{\}]+\ *)",
        "replace": r"htt\1",
    },
    {
        # The [^.] bit at the end of this regex makes sure that we are only replacing h\S\Sps? that are...
        # followed by something other than a period (so as not to change part of a domain name...
        # (see the `test_odd_hXXp_replacement` function in `test_ioc_fanger.py`))
        "find": r"h[xA-Z]{2}(ps?[^.])",
        "replace": r"htt\1",
        "case_sensitive": True,
    },
    {
        "find": r"htt(ps?)\/",
        "replace": r"htt\1:/",
    },
    {
        "find": r"(https?:\/\/)\ *",
        "replace": r"\1",
    },
    {
        "find": r"(https?)\ *:",
        "replace": r"\1:",
    },
    {
        # "xxxx://" -> "http://"
        "find": r"\b(x{4}:\/\/)",
        "replace": "http://",
    },
    {
        # "xxxx[xs]://" -> "https://"
        "find": r"\b((?:x{5}|x{4}s):\/\/)",
        "replace": "https://",
    },
    {
        # Remove brackets around "-"
        "find": r"(\[-\])",
        "replace": "-",
    },
    {
        # Remove whitespace around an @ symbol
        "find": r"(\ +@\ +)",
        "replace": "@",
    },
    {
        # Fang any ip address-esque item with commas between the numbers to have "." between the numbers
        "find": r"(?:^|(?<=\s))([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3}),([0-9]{1,3})(?=\s|$)",
        "replace": r"\1.\2.\3.\4",
    },
    {"find": r"(\\/)", "replace": "/"},
    {"find": r"(\^.)", "replace": "."},
    {"find": r"(\<\.\>)", "replace": "."},
    {
        # "\." -> "."
        "find": r"(\\\.)",
        "replace": ".",
    },
]

fang_mappings = []

for i in fang_patterns:
    flags = re.VERBOSE

    # set all regexes to IGNORECASE by default
    if "case_sensitive" not in i:
        flags = flags | re.IGNORECASE

    mapping = {"find": re.compile(i["find"], flags), "replace": i["replace"]}
    fang_mappings.append(mapping)
