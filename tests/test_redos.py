"""Regression tests for ReDoS (catastrophic backtracking) in ``fang()``.

A small, attacker-controllable input must not pin a CPU for seconds. See the
security review (``report.md``): several fang patterns used a
``\\ *[brackets]*\\ *`` idiom whose two space quantifiers could partition a long
run of spaces in N+1 ways, producing super-polynomial backtracking when the
trailing literal failed to match. Bounding the spaces to ``\\ {0,3}`` keeps
matching linear in the length of the space run.
"""

import threading

import pytest

import ioc_fanger

# Generous ceiling: post-fix these inputs fang in well under a millisecond;
# pre-fix they take many seconds to minutes. 2s cleanly separates the two and
# stays safe on slow CI.
_TIME_BUDGET_SECONDS = 2.0

# Each payload drives a different family of the vulnerable patterns over a long
# whitespace run, then fails the trailing literal to force backtracking:
#   - bracket + spaces (no marker)  -> the ``@``/``at`` and ``AT`` left-group patterns
#   - a ``dot``/``DOT`` marker in the run -> the dot/punto/punkt and DOT patterns
_ADVERSARIAL_INPUTS = [
    "(" + " " * 4000 + "z",
    "(" + " " * 2000 + "dot" + " " * 2000 + "z",
    "-" + " " * 2000 + "DOT" + " " * 2000 + "z",
    " " * 2000 + "at(" + " " * 2000 + "z",
]


@pytest.mark.parametrize(
    "payload",
    _ADVERSARIAL_INPUTS,
    ids=["brackets+spaces", "dot-marker", "DOT-marker", "at-marker"],
)
def test_fang_no_catastrophic_backtracking(payload):
    """fang() returns promptly on adversarial whitespace runs (no ReDoS)."""
    result: list = []

    def _run():
        result.append(ioc_fanger.fang(payload))

    worker = threading.Thread(target=_run, daemon=True)
    worker.start()
    worker.join(_TIME_BUDGET_SECONDS)

    assert not worker.is_alive(), (
        f"fang() did not finish within {_TIME_BUDGET_SECONDS}s on a "
        f"{len(payload)}-byte input - catastrophic backtracking (ReDoS)."
    )
