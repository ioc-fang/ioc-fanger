"""Coverage check: every regex in ioc_fanger must be exercised by at least one test.

The conftest installs tracking proxies around each compiled pattern that record
a hit whenever a substitution actually occurs. This module asserts that every
pattern was hit by the rest of the test suite. The tests in this module are
forced to run last via ``pytest_collection_modifyitems`` in conftest.py.
"""

from ioc_fanger.regexes_fang import fang_patterns
from tests.conftest import DEFANG_HITS, FANG_HITS


def test_all_fang_regexes_exercised():
    expected = set(range(len(fang_patterns)))
    missing = sorted(expected - FANG_HITS)
    if missing:
        details = "\n".join(f"  [{i}] {fang_patterns[i]['find']}" for i in missing)
        raise AssertionError(
            f"{len(missing)} fang regex(es) were never exercised by any test:\n{details}\n"
            "Add a test that triggers a substitution for each pattern above."
        )


def test_all_defang_regexes_exercised():
    expected = {"_dot_re", "_at_re"}
    missing = sorted(expected - DEFANG_HITS)
    assert not missing, f"Defang regex(es) never exercised: {missing}"
