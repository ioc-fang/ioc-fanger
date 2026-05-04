## Development

👋 &nbsp;If you want to contribute to this project, test it locally, or just explore it - we have some helpful instructions below.

### Prerequisites

Install [uv](https://docs.astral.sh/uv/) and then set up your local environment with:

```shell
uv sync --locked --group dev
```

`pyproject.toml` declares the dependency ranges and `uv.lock` pins resolved versions. Both files are kept in sync by `uv` and updated together by Dependabot.

### Test ioc-fanger 🧪

To test ioc-fanger, run the following command from the root directory of the project:

```shell
uv run pytest
```

This runs [pytest][pytest-link] on the project's test suite.

### Lint ioc-fanger 🧹

To lint ioc-fanger, run:

```shell
uv run ruff check ioc_fanger tests
uv run ruff format --check ioc_fanger tests
uv run mypy ioc_fanger tests
```

To auto-fix lint issues and apply formatting, run:

```shell
uv run ruff check --fix ioc_fanger tests
uv run ruff format ioc_fanger tests
```

You can read more about the benefits of linting [here][linting-intro].

### Explore ioc-fanger 🔭

To explore ioc-fanger interactively, drop into an [IPython][ipython] shell with the project and all its requirements loaded:

```shell
uv run ipython
```

[pytest-link]: https://docs.pytest.org/en/stable/
[linting-intro]: https://dbader.org/blog/python-code-linting
[ipython]: https://ipython.org/
