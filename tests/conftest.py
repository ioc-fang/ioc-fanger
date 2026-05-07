import pytest

<<<<<<< ioc-fang-ioc-fanger-92-make-sure-all-regexes-are-tested-claude
from ioc_fanger import ioc_fanger as ioc_fanger_module
from ioc_fanger.regexes_fang import fang_mappings

# Module-level sets recording which regex patterns produced at least one
# substitution during the test session. Populated by the tracking proxies
# installed below; consumed by tests/test_zz_regex_coverage.py.
FANG_HITS: set[int] = set()
DEFANG_HITS: set[str] = set()


class _TrackedFangPattern:
    """Proxy around a compiled fang regex that records substitution hits."""

    def __init__(self, pattern, index: int):
        self._pattern = pattern
        self._index = index

    def sub(self, repl, text):
        new_text, n = self._pattern.subn(repl, text)
        if n > 0:
            FANG_HITS.add(self._index)
        return new_text


class _TrackedDefangPattern:
    """Proxy around a compiled defang regex that records substitution hits."""

    def __init__(self, pattern, name: str):
        self._pattern = pattern
        self._name = name

    def sub(self, repl, text):
        new_text, n = self._pattern.subn(repl, text)
        if n > 0:
            DEFANG_HITS.add(self._name)
        return new_text


# Install tracking proxies. Only happens at test-collection time, so the
# library itself remains uninstrumented when imported by normal callers.
for _i, _mapping in enumerate(fang_mappings):
    _mapping["find"] = _TrackedFangPattern(_mapping["find"], _i)

ioc_fanger_module._dot_re = _TrackedDefangPattern(ioc_fanger_module._dot_re, "_dot_re")  # type: ignore[assignment]
ioc_fanger_module._at_re = _TrackedDefangPattern(ioc_fanger_module._at_re, "_at_re")  # type: ignore[assignment]


def pytest_collection_modifyitems(config, items):
    """Run the regex-coverage tests after everything else has had a chance to hit patterns."""
    coverage_items = [item for item in items if "test_regex_coverage" in item.nodeid]
    other_items = [item for item in items if "test_regex_coverage" not in item.nodeid]
    items[:] = other_items + coverage_items
=======
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
>>>>>>> main


@pytest.fixture
def defanged_text():
    return " ".join([d for d, _ in DEFANG_TO_FANG_PAIRS] + ALREADY_FANGED_STRINGS)


@pytest.fixture
def fanged_text():
    return " ".join([f for _, f in DEFANG_TO_FANG_PAIRS] + ALREADY_FANGED_STRINGS)
