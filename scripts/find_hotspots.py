"""Identify which fang/defang regex pattern is slowest, and back that up
with a cProfile drill-down.

Usage:
    uv run python scripts/find_hotspots.py

Three views are printed:

1. Per-pattern wall time on the long benchmark text. This tells you which
   `find` regex in regexes_fang.py / regexes_defang.py to attack first.
2. Top-level wall time for `fang(text)` and `defang(text)` on both a
   bracket-heavy sample and a bracket-free sample, so you can see how the
   short-circuit path compares to the worst case.
3. Top cumulative-time entries from cProfile across both pipelines. This
   confirms the per-pattern numbers and surfaces which `re` internals each
   pattern is paying for.

Run this before tuning any pattern, and again after, to make sure the
"slow" thing actually moved.
"""

from __future__ import annotations

import cProfile
import io
import os
import pstats
import time
from pathlib import Path

import ioc_fanger
from ioc_fanger.regexes_defang import _at_re, _dot_re
from ioc_fanger.regexes_fang import fang_mappings

TESTS_DIR = Path(os.path.join(os.path.dirname(__file__), "..", "tests"))
LONG_DEFANGED = (TESTS_DIR / "sample_text_defanged.txt").read_text(encoding="utf8")
LONG_FANGED = (TESTS_DIR / "sample_text_fanged.txt").read_text(encoding="utf8")

# A bracket-free sample mimics typical chat/log content that exercises
# the short-circuit path in fang().
BRACKET_FREE = (
    "Visit https://example.com or http://foo.bar to learn more. " * 50
) + ("email me at user@example.com please. " * 50)

REPEATS = 200


def per_fang_pattern_timings(text: str) -> list[tuple[int, str, float]]:
    """Return (index, pattern_snippet, mean_ms_per_run) sorted slowest first."""
    # Warm up so first-call overhead doesn't get charged to whichever
    # pattern happens to run first.
    for m in fang_mappings:
        m["find"].sub(m["replace"], text)

    rows = []
    for i, m in enumerate(fang_mappings):
        find = m["find"]
        replace = m["replace"]
        start = time.perf_counter()
        for _ in range(REPEATS):
            find.sub(replace, text)
        elapsed_ms = (time.perf_counter() - start) / REPEATS * 1000
        snippet = find.pattern.replace("\n", " ").strip()[:70]
        rows.append((i, snippet, elapsed_ms))
    rows.sort(key=lambda r: r[2], reverse=True)
    return rows


def per_defang_step_timings(text: str) -> list[tuple[str, float]]:
    """Return (step_label, mean_ms_per_run) sorted slowest first."""
    _dot_re.sub("[.]", text)
    text.replace("https:", "hXXps:")
    _at_re.sub("(at)", text)

    steps = [
        ("dot regex sub  (?<=\\w)\\.(?=\\w)", lambda t: _dot_re.sub("[.]", t)),
        ("https: -> hXXps: (str.replace)", lambda t: t.replace("https:", "hXXps:")),
        ("http:  -> hXXp:  (str.replace)", lambda t: t.replace("http:", "hXXp:")),
        ("@ regex sub  (?<=\\S)@(?=\\S)", lambda t: _at_re.sub("(at)", t)),
    ]
    rows = []
    for label, fn in steps:
        start = time.perf_counter()
        for _ in range(REPEATS):
            fn(text)
        elapsed_ms = (time.perf_counter() - start) / REPEATS * 1000
        rows.append((label, elapsed_ms))
    rows.sort(key=lambda r: r[1], reverse=True)
    return rows


def end_to_end_timings() -> list[tuple[str, float]]:
    """Wall-clock times for full fang/defang on each sample."""
    cases = [
        ("fang(long_defanged)  [bracket-heavy]", lambda: ioc_fanger.fang(LONG_DEFANGED)),
        ("fang(bracket_free)   [short-circuit]", lambda: ioc_fanger.fang(BRACKET_FREE)),
        ("defang(long_fanged)  [bracket-heavy]", lambda: ioc_fanger.defang(LONG_FANGED)),
        ("defang(bracket_free) [short-circuit]", lambda: ioc_fanger.defang(BRACKET_FREE)),
    ]
    for _, fn in cases:
        fn()

    rows = []
    for label, fn in cases:
        start = time.perf_counter()
        for _ in range(REPEATS):
            fn()
        elapsed_ms = (time.perf_counter() - start) / REPEATS * 1000
        rows.append((label, elapsed_ms))
    return rows


def cprofile_top(n: int = 25) -> str:
    """Run fang+defang through cProfile and return the top-n cumulative entries."""
    ioc_fanger.fang(LONG_DEFANGED)
    ioc_fanger.defang(LONG_FANGED)

    pr = cProfile.Profile()
    pr.enable()
    for _ in range(REPEATS):
        ioc_fanger.fang(LONG_DEFANGED)
        ioc_fanger.fang(BRACKET_FREE)
        ioc_fanger.defang(LONG_FANGED)
        ioc_fanger.defang(BRACKET_FREE)
    pr.disable()

    buf = io.StringIO()
    pstats.Stats(pr, stream=buf).sort_stats("cumulative").print_stats(n)
    return buf.getvalue()


def main() -> None:
    print(f"Long defanged sample: {len(LONG_DEFANGED)} chars")
    print(f"Long fanged sample:   {len(LONG_FANGED)} chars")
    print(f"Bracket-free sample:  {len(BRACKET_FREE)} chars\n")

    print(f"== End-to-end timings (mean of {REPEATS} runs) ==")
    for label, ms in end_to_end_timings():
        print(f"  {label:<42}  {ms:7.3f} ms")

    print(f"\n== Per-fang-pattern timings on long defanged sample (mean of {REPEATS} runs, slowest first) ==")
    rows = per_fang_pattern_timings(LONG_DEFANGED)
    for idx, snippet, ms in rows:
        print(f"  [{idx:2d}]  {ms:7.3f} ms  {snippet!r}")

    print(f"\n== Per-defang-step timings on long fanged sample (mean of {REPEATS} runs, slowest first) ==")
    for label, ms in per_defang_step_timings(LONG_FANGED):
        print(f"  {label:<40}  {ms:7.3f} ms")

    print("\n== cProfile cumulative top entries (fang + defang on both samples) ==")
    print(cprofile_top())


if __name__ == "__main__":
    main()
