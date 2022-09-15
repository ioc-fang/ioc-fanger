from re import IGNORECASE, VERBOSE, compile

# NOTE: Throughout this file, any regex matching a space (e.g. ` *`) must be escaped (e.g. `\ *`) b/c...
# we are compiling in verbose mode (which removes unescaped whitespace)

# workflow: pull next regex out of fang.json and update it here
# - make string raw
# - escape whitespaces
# - escape regex if it doesn't have the "regex" key
# - replace \\ with \
# - remove unneeded keys
# - make sure regex returns a single match group
# - make sure there's a comment

fang_patterns = [
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
        "find": r"((\ *[\[\]\(\)\{\}]*\ *)(?:(?:AT)|(?:rET)|(?:ARROBA))(\ *[\[\]\(\)\{\}]+\ *))",
        "replace": "@",
        "case_sensitive": True,
    },
    {
        # Fang "www" surrounded by any kind of bracket
        "find": r"(([\[\]\(\)\{\}]{1}\ *)www(\ *[\[\]\(\)\{\}]{1}\ *))",
        "replace": "www",
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
    {"find": r"(\\/)", "replace": "/"},
    {"find": r"(\^.)", "replace": "."},
    {"find": r"(\<\.\>)", "replace": "."},
]

fang_mappings = []

for i in fang_patterns:
    flags = VERBOSE

    # set all regexes to IGNORECASE by default
    if "case_sensitive" not in i:
        flags = flags | IGNORECASE

    mapping = {"find": compile(i["find"], flags), "replace": i["replace"]}
    fang_mappings.append(mapping)
