# IOC Fanger

[![PyPi](https://img.shields.io/pypi/v/ioc_fanger.svg)](https://pypi.python.org/pypi/ioc_fanger)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ioc-fanger)
[![CI](https://github.com/ioc-fang/ioc-fanger/workflows/CI/badge.svg)](https://github.com/ioc-fang/ioc-fanger/actions)
[![Lint](https://github.com/ioc-fang/ioc-fanger/workflows/Lint/badge.svg)](https://github.com/ioc-fang/ioc-fanger/actions)
[![Codecov](https://codecov.io/gh/ioc-fang/ioc-fanger/branch/master/graph/badge.svg)](https://codecov.io/gh/ioc-fang/ioc-fanger)
[![live demo](https://img.shields.io/badge/live%20demo-%E2%86%92-green)](http://ioc-fanger.hightower.space/)

Python package to fang (`example[.]com => example.com`) and defang (`example.com => example[.]com`) [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) in text.

Read more in our [interactive documentation](http://ioc-fanger.hightower.space/)!

## What can be fanged?

`ioc_fanger.fang` recognises the following defanging patterns and restores them to their normal form:

- Brackets, parentheses, or braces around a `.` or `,` &mdash; e.g. `example[.]com`, `example(.)com`, `example{.}com`, `example[,]com`
- Brackets, parentheses, or braces around a `:` &mdash; e.g. `http[:]//example.com`
- The literal word `DOT`, `dot`, `punto`, or `punkt` standing in for a `.` &mdash; e.g. `example[dot]com`, `example DOT com`, `example-punto-com`
- Brackets, parentheses, or braces around `://` &mdash; e.g. `http[://]example.com`
- Brackets, parentheses, or braces around `www` &mdash; e.g. `[www]example.com`
- Brackets, parentheses, or braces around a `-` &mdash; e.g. `service[-]ict.nl`
- `@` replaced with `at`, `et`, `arroba`, or `@` itself wrapped in brackets/parentheses/braces &mdash; e.g. `user[at]example.com`, `user(@)example.com`, `user AT example.com`
- Defanged URL schemes such as `hXXp://`, `hXXps://`, `hxxp://`, `xxxx://`, `xxxxs://`, `xxxx[s]://`, as well as bracketed variants like `[http]://` and `htt[p]://`
- URL schemes split by extra slashes or whitespace &mdash; e.g. `http:///example.com`, `http: //example.com`, `https :  //example.com`
- IPv4 addresses written with commas instead of dots &mdash; e.g. `8,8,8,8` &rarr; `8.8.8.8`
- Backslash-, caret-, or angle-bracket-escaped dots &mdash; e.g. `example\.com`, `example^.com`, `example<.>com`
- Backslash-escaped slashes &mdash; e.g. `http:\/\/example.com`
- Stray whitespace around an `@` in an email &mdash; e.g. `user @ example.com`

These patterns combine, so inputs like `hXXp://bad[.]example[dot]com/file[.]php` are fully restored in a single call.

## What can be defanged?

`ioc_fanger.defang` applies a small, deliberately conservative set of substitutions so the output is unambiguous to re-fang:

- A `.` between two word characters becomes `[.]` &mdash; e.g. `example.com` &rarr; `example[.]com`, `8.8.8.8` &rarr; `8[.]8[.]8[.]8`
- The URL schemes `http:` and `https:` become `hXXp:` and `hXXps:` &mdash; e.g. `http://example.com` &rarr; `hXXp://example[.]com`
- An `@` between two non-whitespace characters becomes `(at)` &mdash; e.g. `user@example.com` &rarr; `user(at)example[.]com`

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
