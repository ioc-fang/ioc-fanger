from re import VERBOSE, compile

# NOTE: Throughout this file, any regex matching a space (e.g. ` *`) must be escaped (e.g. `\ *`) b/c...
# we are compiling in verbose mode (which removes unescaped whitespace)

# todo: handle case sensitiveness here rather than in ioc_fanger.py
# workflow: pull next regex out of fang.json and update it here

fang_patterns = [
    {
        # "[://]" -> "://"
        "find": r"(\[:\/\/\])", "replace": "://"},
    {
        # Fang a period or comma preceeded and postceded by any kind of bracket
        # We don't allow spaces after the "." so we don't inadvertantly fang valid sentences...
        # (e.g. we don't want to fang something like: "an example). [B]")
        "find": r"((\ *[\[\]\(\)\{\}]{1}\ *)[.,]([\[\]\(\)\{\}]{1}\ *))",
        "replace": ".",
    },
    {
        # Fang a colon preceeded and postceded by parenthesis or square brackets.
        "find": r"((\ *[\[\]\(\)\{\}]{1}\ *):(\ *[\[\]\(\)\{\}]{1}\ *))",
        "replace": ":",
    },
    {
        # Remove whitespace around an @ symbol
        "find": r"(\ +@\ +)",
        "replace": "@",
    },
]

fang_mappings = [{"find": compile(i["find"], VERBOSE), "replace": i["replace"]} for i in fang_patterns]

