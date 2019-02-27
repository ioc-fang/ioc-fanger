# IOC Fanger

[![PyPi](https://img.shields.io/pypi/v/ioc_fanger.svg)](https://pypi.python.org/pypi/ioc_fanger)
[![Travis CI](https://img.shields.io/travis/ioc-fang/ioc_fanger.svg)](https://travis-ci.org/ioc-fang/ioc_fanger)
[![Codecov](https://codecov.io/gh/ioc-fang/ioc_fanger/branch/master/graph/badge.svg)](https://codecov.io/gh/ioc-fang/ioc_fanger)
[![Codacy](https://api.codacy.com/project/badge/Grade/d1762339ba454fba87c02a1b7ea69052)](https://www.codacy.com/app/fhightower/ioc_fanger)

Python package to fang and defang [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) in text. You can test out this project here: [http://ioc-fanger.hightower.space](http://ioc-fanger.hightower.space).

**Defanging** - converting indicators of compromise from the normal form (which can become links) to a form which cannot accidentally become a link:

`example.com => example[.]com`

**Fanging** - converting indicators of compromise from a defanged form to the normal, original form:

`example[.]com => example.com`

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

-   `fang`
-   `defang`

After each command, provide the text you would like to fang/defang:

``` {.sourceCode .shell}
fang "example[.]com"  # example.com
```

``` {.sourceCode .shell}
defang "example.com"  # example[.]com
```

## Adding More Fanging/Defanging Options

You can view the current fanging patterns [here](https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/fang.json) and the defanging patterns [here](https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/defang.json).

To add more fanging options, edit [fang.json](https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/fang.json) and add an entry for the new pattern you would like to fang. The available keys for each entry are:

-   `find` (required): This is the string pattern you would like to find
-   `replace` (required): This is the string used to replace all instances to pattern specified by the `find` key
-   `case_sensitive` (optional - boolean): If this is `true`, the pattern specified by the `find` key will be treated as case sensitive (it will only be replaced if the case is an exact match)
-   `regex` (optional - boolean): If this is `true`, the pattern specified by the `find` key will be treated as a regex (it will not be escaped before use)

## Other Helpful Projects

If you are working with IOCs, you may find the [https://github.com/fhightower/ioc-finder](https://github.com/fhightower/ioc-finder) project helpful. It is a project designed to parse indicators of compromise from text (it uses grammars rather than regexes).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [fhightower/python-project-template](https://gitlab.com/fhightower/python-project-template) project template.
