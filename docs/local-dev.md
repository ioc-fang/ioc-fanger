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

### Run the docs 📖

To preview the documentation site locally with live reload, run:

```shell
uv run mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Explore ioc-fanger 🔭

To explore ioc-fanger interactively, drop into an [IPython][ipython] shell with the project and all its requirements loaded:

```shell
uv run ipython
```

### Benchmarks 📈

Benchmarks live in `tests/benchmarks.py` and are kept out of the default `pytest` run. Saved baselines for each platform live under `.benchmarks/` (e.g. `Darwin-CPython-3.14-64bit/0001_benchmark.json`, `Linux-CPython-3.14-64bit/0001_benchmark.json`).

To **compare** against the macOS baseline locally:

```shell
uv run pytest -c "." --benchmark-storage=.benchmarks/Darwin-CPython-3.14-64bit/ --benchmark-compare=0001 --benchmark-compare-fail=mean:30% --benchmark-columns='mean,stddev,median,iqr,outliers' tests/benchmarks.py
```

To **regenerate** the macOS baseline:

```shell
uv run pytest -c "." --benchmark-storage=.benchmarks/ --benchmark-save=benchmark tests/benchmarks.py
# then move the resulting file to .benchmarks/Darwin-CPython-3.14-64bit/0001_benchmark.json
```

Linux benchmarks must be generated/compared inside Docker so the environment matches CI. From the repo root:

```shell
docker compose run --rm test-benchmarks    # compare against the saved Linux baseline
docker compose run --rm update-benchmarks  # regenerate the Linux baseline at .benchmarks/Linux-CPython-3.14-64bit/0001_benchmark.json
```

[pytest-link]: https://docs.pytest.org/en/stable/
[linting-intro]: https://dbader.org/blog/python-code-linting
[ipython]: https://ipython.org/
