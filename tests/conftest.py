import pytest

# (defanged_input, expected_fanged_output) — strings that fang() should transform
DEFANG_TO_FANG_PAIRS = [
    ("example[.]com", "example.com"),
    ("hxxp://example[.]com", "http://example.com"),
    ("hXXp://example[.]com", "http://example.com"),
    ("example\\.com", "example.com"),
    ("example^.com", "example.com"),
    ("hxxp://example[.]com", "http://example.com"),
    ("1[.]2[.]3[.]4", "1.2.3.4"),
    ("bob[@]example[.]com", "bob@example.com"),
    ("mary[@]example.com", "mary@example.com"),
    ("carlos[at]example.com", "carlos@example.com"),
    ("juanita(at)example.com", "juanita@example.com"),
    ("http[:]//example.org", "http://example.org"),
    ("https[:]//example.org", "https://example.org"),
    ("hXxps[:]//example.org/test?target=bad[@]test.com", "https://example.org/test?target=bad@test.com"),
    ("bad-dot-com", "bad.com"),
    ("example-dot-ru", "example.ru"),
    ("5[,]6[,]7(,)8", "5.6.7.8"),
    ("9,10,11,12", "9.10.11.12"),
]

# strings that are already fanged and should pass through fang() unchanged
ALREADY_FANGED_STRINGS = [
    "example.com",
    "http://example.com",
]


@pytest.fixture
def defanged_text():
    return " ".join([d for d, _ in DEFANG_TO_FANG_PAIRS] + ALREADY_FANGED_STRINGS)


@pytest.fixture
def fanged_text():
    return " ".join([f for _, f in DEFANG_TO_FANG_PAIRS] + ALREADY_FANGED_STRINGS)
