# pyproject_template


This is a template for a Python project I use in as base for my personal projects.
It is based on best practices I use in most of my projects.

I based on [cookiecutter](https://github.com/cookiecutter/cookiecutter) tool to create this template.

# Quick Start
Install the latest Cookiecutter if you haven't installed it yet:
```bash
pip install -U cookiecutter
```

Generate a Python package project:
```bash
cookiecutter gh:perchick03/pln-proj-template-py
```

# Features


# Requirements
* Python 3.7+
* [cookiecutter](https://github.com/cookiecutter/cookiecutter)
* setuptools

`pip install --user cookiecutter`

# Usage

`cookiecutter gh:perchick03/pln-proj-template-py`

# Details

## Tools
### pre-commit
installation
```bash
pip install pre-commit
# setup pre-commit hooks
pre-commit install
```
run pre-commit hooks
```bash
pre-commit run --all-files
```
