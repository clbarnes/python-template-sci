# python-template-sci

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for exploratory scientific python projects.

Ensure you have `cookiecutter` installed, then do

```sh
cookiecutter gh:clbarnes/python-template-sci
```

Originally forked from [clbarnes/python-template](https://github.com/clbarnes/python-template).

## Features

- Pre-populated data and credentials directories with appropriate gitignores
- Simple dependency listing using `requirements.txt` and [extreqs](https://pypi.org/project/extreqs/)
- CI/CD with [GitHub Actions](https://docs.github.com/en/actions)
- Unit tests with [pytest](https://docs.pytest.org/)
- Linting with [flake8](https://pypi.org/project/flake8/), formatting with [black](https://pypi.org/project/black/) and [isort](https://pypi.org/project/isort/)
- Version management with [setuptools-scm](https://pypi.org/project/setuptools-scm/)
- Containerisation with [apptainer](https://apptainer.org/docs/user/main/introduction.html)
- [Makefile](https://www.gnu.org/software/make/) for common tasks
- Verson control with [git](https://git-scm.com/)
- README.md with in-depth usage and development notes
