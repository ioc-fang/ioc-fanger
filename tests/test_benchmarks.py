"""Run some long tests with benchmarking to test how long the library takes to run."""

import os

import ioc_fanger

SAMPLE_TEXT_FANGED_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample_text_fanged.txt'))
SAMPLE_TEXT_DEFANGED_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample_text_defanged.txt'))

with open(SAMPLE_TEXT_FANGED_FILE_PATH) as f:
    SAMPLE_TEXT_FANGED = f.read()

with open(SAMPLE_TEXT_DEFANGED_FILE_PATH) as f:
    SAMPLE_TEXT_DEFANGED = f.read()


def fang_benchmark():
    return ioc_fanger.fang(SAMPLE_TEXT_DEFANGED)


def test_fanging__benchmark(benchmark):
    """Test fanging."""
    test_fanged_text = benchmark(fang_benchmark)
    print(test_fanged_text)
    assert test_fanged_text == SAMPLE_TEXT_FANGED


def defang_benchmark():
    return ioc_fanger.defang(SAMPLE_TEXT_FANGED)


def test_defanging__benchmark(benchmark):
    """Test defanging."""
    test_defanged_text = benchmark(defang_benchmark)
    print(test_defanged_text)
    assert test_defanged_text == SAMPLE_TEXT_DEFANGED
