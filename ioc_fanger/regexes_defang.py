import re

defang_patterns = [
    {
        # "example.com" -> "example[.]com"
        "find": r"""
            (?<=\w)  # positive lookbehind making sure the "." is preceded by a word character
            (\.)  # match a "." character
            (?=\w)  # positive ahead making sure the "." is postceded by a word character
        """,
        "replace": "[.]",
    },
    # "http://example.com" -> "hXXp://example.com"
    {"find": "http:", "replace": "hXXp:"},
    # "https://example.com" -> "hXXps://example.com"
    {"find": "https:", "replace": "hXXps:"},
    # "foo@example.com" -> "foo(at)example.com"
    {"find": r"(?<=\S)(@)(?=\S)", "replace": "(at)"},
]

defang_mappings = [{"find": re.compile(i["find"], re.VERBOSE), "replace": i["replace"]} for i in defang_patterns]
