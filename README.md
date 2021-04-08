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

Once you install the package, there will be two commands available in the command line:

- `fang`
- `defang`

After each command, provide the text you would like to fang/defang:

``` {.sourceCode .shell}
fang "example[.]com"  # example.com
```

``` {.sourceCode .shell}
defang "example.com"  # example[.]com
```

## Development

👋 &nbsp;If you want to contribute to this project, test it locally, or just explore it - we have some helpful instructions below.

### Prerequisites

If you want to test, lint, or explore a project, make sure you have [docker][docker] and [docker-compose][docker-compose] installed (if you don't see: [installing docker][docker-install]).

Then you can use the **test**, **lint**, and **dev** docker compose services listed below!

### Test a Project 🧪

To test a project, run the following command from the root directory of the project:

```shell
docker-compose run --rm test
```

Typically, this command will run [pytest][pytest-link] on the project's test suite. To view the details of what this command does, take a look at the `test` service in the project's `docker-compose.yml` file.

### Lint a Project 🧹

To lint a project, run the following command from the root directory of the project:

```shell
docker-compose run --rm lint
```

Typically, this command will run linters on the project's code with the goal of improving code quality and catching bugs before we release them (you can read more about the benefits of linting [here][linting-intro]). To view the details of what this command does, take a look at the `lint` service in the project's `docker-compose.yml` file.

### Explore a Project 🔭

To explore a project, you can drop into a "dev" environment which is an [IPython][ipython] shell with the project and all its requirements loaded. To do this, run the following command from the root directory of the project:

```shell
docker-compose run --rm dev
```

To see what this command does, take a look at the `dev` service in the project's `docker-compose.yml` file.

## Feedback

If you have any ideas to improve this package, please raise an issue!

## Other Helpful Projects

If you are working with indicators of compromise (a.k.a. observables), you may find the [ioc-finder](https://github.com/fhightower/ioc-finder) project helpful. The ioc-finder project parses indicators of compromise from text (using grammars).

## Credits

We created this package using [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [fhightower/python-project-template](https://github.com/fhightower/python-project-template) project template.

[pytest-link]: https://docs.pytest.org/en/stable/
[docker-compose]: https://docs.docker.com/compose/
[docker-install]: https://docs.docker.com/get-docker/
[docker]: https://www.docker.com/get-started
[linting-intro]: https://dbader.org/blog/python-code-linting
[ipython]: https://ipython.org/
