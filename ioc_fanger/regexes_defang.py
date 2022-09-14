from re import VERBOSE, compile

defang_patterns = [
    {
        # "example.com" -> "example[.]com"
        "find": r"""
            # match any "." character directly before certain word characters
            (\.)
            [a-zA-Z0-9-]
        """,
        "replace": "[.]",
    },
    # "http://example.com" -> "hXXp://example.com"
    {"find": "(http:)", "replace": "hXXp:"},
    # "https://example.com" -> "hXXps://example.com"
    {"find": "(https:)", "replace": "hXXps:"},
    # "foo@example.com" -> "foo(at)example.com"
    {"find": r"\S(@)\S", "replace": "(at)"},
]

defang_mappings = [{"find": compile(i["find"], VERBOSE), "replace": i["replace"]} for i in defang_patterns]
