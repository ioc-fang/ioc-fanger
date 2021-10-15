## Development

👋 &nbsp;If you want to contribute to this project, test it locally, or just explore it - we have some helpful instructions below.

### Prerequisites

If you want to test, lint, or explore ioc-fanger, make sure you have [docker][docker] and [docker-compose][docker-compose] installed (if you don't see: [installing docker][docker-install]).

Then you can use the **test**, **lint**, and **dev** docker compose services listed below!

### Test ioc-fanger 🧪

To test ioc-fanger, run the following command from the root directory of the project:

```shell
docker-compose run --rm test
```

Typically, this command will run [pytest][pytest-link] on the project's test suite. To view the details of what this command does, take a look at the `test` service in the project's `docker-compose.yml` file.

### Lint ioc-fanger 🧹

To lint ioc-fanger, run the following command from the root directory of the project:

```shell
docker-compose run --rm lint
```

Typically, this command will run linters on the project's code with the goal of improving code quality and catching bugs before we release them (you can read more about the benefits of linting [here][linting-intro]). To view the details of what this command does, take a look at the `lint` service in the project's `docker-compose.yml` file.

### Explore ioc-fanger 🔭

To explore ioc-fanger, you can drop into a "dev" environment which is an [IPython][ipython] shell with the project and all its requirements loaded. To do this, run the following command from the root directory of the project:

```shell
docker-compose run --rm dev
```

To see what this command does, take a look at the `dev` service in the project's `docker-compose.yml` file.

[pytest-link]: https://docs.pytest.org/en/stable/
[docker-compose]: https://docs.docker.com/compose/
[docker-install]: https://docs.docker.com/get-docker/
[docker]: https://www.docker.com/get-started
[linting-intro]: https://dbader.org/blog/python-code-linting
[ipython]: https://ipython.org/
