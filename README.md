# IOC Fanger

[![PyPi](https://img.shields.io/pypi/v/ioc_fanger.svg)](https://pypi.python.org/pypi/ioc_fanger)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ioc-fanger)
[![Travis CI](https://img.shields.io/travis/ioc-fang/ioc_fanger.svg)](https://travis-ci.org/ioc-fang/ioc_fanger)
[![Codecov](https://codecov.io/gh/ioc-fang/ioc_fanger/branch/master/graph/badge.svg)](https://codecov.io/gh/ioc-fang/ioc_fanger)
[![live demo](https://img.shields.io/badge/live%20demo-%E2%86%92-green)](http://ioc-fanger.hightower.space/)

Python package to fang and defang [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) in text.

```python
import ioc_fanger

ioc_fanger.defang("example.com http://bad.com/phishing.php")  # example[.]com hXXp://bad[.]com/phishing[.]php
ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")  # example.com http://bad.com/phishing.php
```

**Defanging** - converting indicators of compromise from the normal form (which can become links) to a form which cannot accidentally become a link:

`example.com => example[.]com`

**Fanging** - converting indicators of compromise from a defanged form to the normal, original form:

`example[.]com => example.com`

<!-- TODO: list out the type of things which can be fanged -->

**What can it fang?**

Just about everything. Check out the [tests](https://github.com/ioc-fang/ioc_fanger/blob/master/tests/test_ioc_fanger.py) to see some examples of what this package can handle.

## Installation

The recommended means of installation is using [pip](https://pypi.python.org/pypi/pip/):

`pip install ioc_fanger`

Alternatively, you can install ioc\_fanger as follows:

```shell
git clone https://github.com/ioc-fang/ioc_fanger.git && cd ioc_fanger;
python setup.py install --user;
```

## Usage

### Via Python

Use ioc\_fanger as follows:

```python
import ioc_fanger

ioc_fanger.defang("example.com http://bad.com/phishing.php")  # example[.]com hXXp://bad[.]com/phishing[.]php
ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")  # example.com http://bad.com/phishing.php
```

### Via Command Line

Once the package is installed, there will be two commands available in the command line:

- `fang`
- `defang`

After each command, provide the text you would like to fang/defang:

``` {.sourceCode .shell}
fang "example[.]com"  # example.com
```

``` {.sourceCode .shell}
defang "example.com"  # example[.]com
```

## Feedback

If you have any ideas to improve this package, please raise an issue!

## Other Helpful Projects

If you are working with observables (a.k.a. indicators of compromise), you may find the [https://github.com/fhightower/ioc-finder](https://github.com/fhightower/ioc-finder) project helpful. It is a project designed to parse indicators of compromise from text (it uses grammars rather than regexes).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [fhightower/python-project-template](https://gitlab.com/fhightower/python-project-template) project template.
