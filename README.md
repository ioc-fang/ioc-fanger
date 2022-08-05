# IOC Fanger

[![PyPi](https://img.shields.io/pypi/v/ioc_fanger.svg)](https://pypi.python.org/pypi/ioc_fanger)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ioc-fanger)
[![CI](https://github.com/ioc-fang/ioc-fanger/workflows/CI/badge.svg)](https://github.com/ioc-fang/ioc-fanger/actions)
[![Lint](https://github.com/ioc-fang/ioc-fanger/workflows/Lint/badge.svg)](https://github.com/ioc-fang/ioc-fanger/actions)
[![Codecov](https://codecov.io/gh/ioc-fang/ioc-fanger/branch/master/graph/badge.svg)](https://codecov.io/gh/ioc-fang/ioc-fanger)
[![live demo](https://img.shields.io/badge/live%20demo-%E2%86%92-green)](http://ioc-fanger.hightower.space/)

Python package to fang (`example[.]com => example.com`) and defang (`example.com => example[.]com`) [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) in text.

Read more in our [interactive documentation](http://ioc-fanger.hightower.space/)!

## Developer Docs

For those working on or testing this library, here's some helpful tips.

### Updating Benchmarks

This project uses [pytest-benchmark](https://pypi.org/project/pytest-benchmark/) to test the performance impact of changes.

By default, every time you run tests it will compare the new results with the existing results.

If you need to update the benchmarks, open the `pyproject.toml` and replace all flags starting with `--benchmark` with:

```
--benchmark-save=benchmark
```

This will save a file in the `.benchmarks/` dir.
