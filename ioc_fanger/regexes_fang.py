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
        "requires_brackets": True,
    },
    {
        # Fang a period or comma surrounded by any kind of bracket
        # We don't allow spaces after the "." so we don't inadvertently fang valid sentences...
        # (e.g. we don't want to fang something like: "an example). [B]")
        "find": r"((\ {0,3}[\[\]\(\)\{\}]{1}\ {0,3})[.,]([\[\]\(\)\{\}]{1}\ {0,3}))",
        "replace": ".",
        "requires_brackets": True,
    },
    {
        # Fang a colon surrounded by any kind of bracket
        "find": r"((\ {0,3}[\[\]\(\)\{\}]{1}\ {0,3}):(\ {0,3}[\[\]\(\)\{\}]{1}\ {0,3}))",
        "replace": ":",
        "requires_brackets": True,
    },
    {
        # Fang "DOT" surrounded by brackets/hyphens (1+ on the left)
        "find": r"((\ {0,3}[\[\]\(\)\{\}-]+\ {0,3})DOT(\ {0,3}[\[\]\(\)\{\}-]*\ {0,3}))",
        "replace": ".",
        "case_sensitive": True,
        "requires_any": ["DOT"],
    },
    {
        # Fang "DOT" surrounded by brackets/hyphens (1+ on the right)
        "find": r"((\ {0,3}[\[\]\(\)\{\}-]*\ {0,3})DOT(\ {0,3}[\[\]\(\)\{\}-]+\ {0,3}))",
        "replace": ".",
        "case_sensitive": True,
        "requires_any": ["DOT"],
    },
    {
        # Fang bare "DOT" only when it sits inside a token that has no real `.`...
        # and is not adjacent to other uppercase letters. This keeps `fooDOTcom` and...
        # `foo@barDOTcom` working while preserving real-world tokens like `MDOT` in...
        # `WWW.MDOT.JXCSF.VIP` (see ioc-fang/ioc-fanger#112).
        "find": r"(?<!\S)([^\s.]*?)\ *(?<![A-Z])DOT(?![A-Z])\ *([^\s.]*?)(?!\S)",
        "replace": r"\1.\2",
        "case_sensitive": True,
        "requires_any": ["DOT"],
    },
    {
        # Fang dot/punto/punkt preceded by 1+ bracket (and perhaps postceded by brackets)
        "find": r"((\ {0,3}[\[\]\(\)\{\}]+\ {0,3})(?:dot|punto|punkt)(\ {0,3}[\[\]\(\)\{\}]*\ {0,3}))",
        "replace": ".",
        "requires_any": ["dot", "punto", "punkt"],
    },
    {
        # Fang dot/punto/punkt postceded by 1+ bracket (and perhaps preceded by brackets)
        "find": r"((\ {0,3}[\[\]\(\)\{\}]*\ {0,3})(?:dot|punto|punkt)(\ {0,3}[\[\]\(\)\{\}]+\ {0,3}))",
        "replace": ".",
        "requires_any": ["dot", "punto", "punkt"],
    },
    {
        # Fang dot/punto/punkt with hyphens on BOTH sides (e.g. `foo-dot-com`).
        # Hyphens on only one side are not treated as defang markers, so strings...
        # like `accounts.dot-star.online` are preserved (ioc-fang/ioc-fanger#112).
        "find": r"-+(?:dot|punto|punkt)-+",
        "replace": ".",
        "requires_any": ["dot", "punto", "punkt"],
    },
    {
        # Fang any of the words in the middle of the regex preceded (and perhaps postceded) by any kind of bracket
        "find": r"((\ {0,3}[\[\]\(\{\}]+\ {0,3})(?:@|(?:at)|(?:et)|(?:arroba))(\ {0,3}[\]\(\)\{\}]*\ {0,3}))",
        "replace": "@",
        "case_sensitive": True,
        "requires_brackets": True,
    },
    {
        # Fang any of the words in the middle of the regex postceded (and perhaps preceded) by any kind of bracket
        "find": r"((\ {0,3}[\[\]\(\)\{\}]*\ {0,3})(?:@|(?:at)|(?:et)|(?:arroba))(\ {0,3}[\]\(\)\{\}]+\ {0,3}))",
        "replace": "@",
        "case_sensitive": True,
        "requires_brackets": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' preceded by a parenthesis/square brackets and possibly postceded by the same.
        "find": r"((\ {0,3}[\[\]\(\)\{\}]+\ {0,3})(?:(?:AT)|(?:ET)|(?:ARROBA))(\ {0,3}[\[\]\(\)\{\}]*\ {0,3}))",
        "replace": "@",
        "case_sensitive": True,
        "requires_brackets": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' postceded by a parenthesis/square brackets and possibly preceded by the same.
        "find": r"((\ {0,3}[\[\]\(\)\{\}]*\ {0,3})(?:(?:AT)|(?:ET)|(?:ARROBA))(\ {0,3}[\[\]\(\)\{\}]+\ {0,3}))",
        "replace": "@",
        "case_sensitive": True,
        "requires_brackets": True,
    },
    {
        # Fang 'AT', 'ET', or 'ARROBA' preceded by a lower-cased character (and possibly spaces)
        "find": r"([a-z])\ *(?:AT|ET|ARROBA)\ *([a-z])",
        "replace": r"\1@\2",
        "case_sensitive": True,
        "requires_any": ["AT", "ET", "ARROBA"],
    },
    {
        # Fang "www" surrounded by any kind of bracket
        "find": r"(([\[\]\(\)\{\}]{1}\ {0,3})www(\ {0,3}[\[\]\(\)\{\}]{1}\ {0,3}))",
        "replace": "www",
        "requires_brackets": True,
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
        "find": r"(?:[\[\(\{]+\ {0,3})htt(ps?)(?:\ {0,3}[\[\]\(\)\{\}]*\ {0,3})",
        "replace": r"htt\1",
        "requires_brackets": True,
    },
    {
        # Fang "https?" postceded by a parenthesis/square brackets and possibly preceded by the same.
        "find": r"(?:[\[\]\(\)\{\}]*\ {0,3})htt(ps?)(?:\ {0,3}[\[\]\(\)\{\}]+\ {0,3})",
        "replace": r"htt\1",
        "requires_brackets": True,
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
        "requires_any": ["xxxx"],
    },
    {
        # "xxxx[xs]://" -> "https://"
        "find": r"\b((?:x{5}|x{4}s):\/\/)",
        "replace": "https://",
        "requires_any": ["xxxx"],
    },
    {
        # Remove brackets around "-"
        "find": r"(\[-\])",
        "replace": "-",
        "requires_brackets": True,
    },
    {
        # Remove whitespace around an @ symbol
        "find": r"(\ +@\ +)",
        "replace": "@",
    },
    {
        # Fang any ip address-esque item with commas between the numbers to have "." between the numbers.
        # Each octet is constrained to 0-255 so we don't match obvious non-IPs like "999,999,999,999".
        "find": (
            r"(?:^|(?<=\s))"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),"
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
            r"(?=\s|$)"
        ),
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
    case_sensitive = "case_sensitive" in i
    if not case_sensitive:
        flags = flags | re.IGNORECASE

    mapping = {"find": re.compile(i["find"], flags), "replace": i["replace"]}
    if i.get("requires_brackets"):
        mapping["requires_brackets"] = True
    # `requires_any` lists literal substrings, at least one of which must be
    # present in the text for this mapping to possibly match. When none are
    # present the substitution is a guaranteed no-op, so `fang()` skips it (the
    # same optimization as `requires_brackets`). `gate_case_sensitive` tells
    # `fang()` how to look for those literals: case-sensitive mappings are
    # matched verbatim, case-insensitive ones against a lower-cased copy of the
    # text (so the literals here must be lower-case). It is named distinctly
    # from the pattern dict's `case_sensitive` key — which controls IGNORECASE
    # at compile time above — because it only routes the literal gate.
    if "requires_any" in i:
        mapping["requires_any"] = i["requires_any"]
        mapping["gate_case_sensitive"] = case_sensitive
    fang_mappings.append(mapping)
