# Design Document for Python Project Template

## Introduction

This design document outlines the architecture and implementation details for a Python project template. The template will provide a simple and fast way to deploy a Python project with a basic setup, including tools and Continuous Integration/Continuous Deployment (CI/CD) support. The primary goal of this project is to save time setting up new projects by providing a single point for change where best practices and new tools can be introduced and applied to all feature projects. This document provides an overview of the system, including its functional and non-functional requirements, constraints, dependencies, and risks. It is intended to guide the implementation and development of the system to meet the desired goals.

## System Architecture and Design

### Project Template

The project template will be generated based on the library [cookiecutter](https://github.com/cookiecutter/cookiecutter). Cookiecutter generates template projects based on [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) and has a lot of [template projects](https://github.com/search?q=cookiecutter&type=Repositories) available on GitHub. The `pln-proj-template` template will be located in GitHub since cookiecutter is built on top of GitHub templates. Cookiecutter receives user input and replaces placeholder names in the template with the user-supplied input.

To use the template, the user can install cookiecutter and run the following command, which will prompt them for the project name and other metadata:

bashCopy code

`cookiecutter gh:perchick03/perchick03/pln-proj-template-py`

The directory structure required by cookiecutter looks as follows:

```text
pln-proj-template-pln/
├── {{ cookiecutter.project_name }}/  <--------- Project template
│   └── ...
├── blah.txt                      <--------- Non-templated files/dirs
│                                            go outside
│
└── cookiecutter.json             <--------- Prompts & default values

```
The output for a project named `template-proj-demo` will be:

```text
template-proj-demo/  <---------- Project name given by the user
│
└── ...       <-------- Files corresponding to those in your
                        cookiecutter's `{{ cookiecutter.project_name }}/` dir

```


Possible Configuration File
```json

```

### Project Filesystem Layout

The filesystem layout for the Python project will use the flat layout. The flat layout is simple and easy to understand. Here is an example of the flat layout for an `awesome_package` project:

```text
.
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── awesome_package/
│   ├── __init__.py
│   └── module.py

```
### Generated Project Building

This component will enable the generated project to be built into a valid Python wheel (`.whl`) package and `sdist` package. The build system chosen is setuptools. All information regarding the project metadata and build information will be stored in `pyproject.toml`. To build a wheel, the user can run `python3 build wheel sdist` from the generated project root (where `pyproject.toml` is located).

### Versioning Strategy

The versioning strategy for the project will use semantic versioning (MAJOR.MINOR.PATCH) using single sourcing for package version. [Setuptools-scm](https://pypi.org/project/setuptools-scm/) will be used for versioning. This assumes that the user is using the project

### Dependency Management

This component will manage project dependencies for production and development. Dependencies for production will be listed in a `requirements.txt` file at the project root, while development dependencies will be listed in a separate `requirements-dev.txt` file. The dependencies listed in `requirements.txt` will be automatically generated and included in the `pyproject.toml` file using the following code:

```toml
[tool.setuptools.dynamic]
dependencies = {file = ["requirements.txt"]}
```


This will ensure that dependencies are properly managed and included in the project as needed.

### Python Entry Point Script

-   The component will provide a CLI entry point script for the project with the command `<project_name>_cli`.
-   The script will include the following optional flags:
    -   `--help` to show the help message for the command
    -   `--version` to display the package version
    -   `--run-test` to run package tests (only available in development mode).

## Design Section - GitLab CICD Pipeline

This design section outlines the setup for the GitLab CICD pipeline for a project, including the registry used, pipeline stages, and job triggers. The CICD pipeline is responsible for continuous integration and deployment of the project.

### Registry

The PyPi registry will be used by default for newly created packages in the CICD pipeline. The package will be pushed automatically to GitLab PyPi when a new tag is pushed. Additionally, the GitLab Docker registry will be used to store the GitLab development image.

### Pipeline Stages

The GitLab CICD pipeline will consist of four stages: Build, Test, Deploy, and Report.

#### Build Stage

The Build stage is responsible for building project artifacts and validating them. This stage will consist of three jobs:

-   GitLab development docker image build: This job will be triggered on each change to `gitlab/Dockerfile.dev`, changes to `requirements-dev.txt`, or if explicitly triggered. The resulting image will be pushed to the GitLab Docker registry.
-   Wheel, sdist package: This job will build, validate, and upload wheel and sdist packages to the GitLab PyPi registry. On a git tag change, the artifacts will also be pushed to the registry.
-   Documentation: This job will generate project documentation on each merge to the master branch.

#### Test Stage

The Test stage is responsible for running tests on the project. This stage will consist of three jobs:

-   Unit tests: This job will run unit tests using pytest and tox.
-   Integration tests: This job will run integration tests using pytest and tox.
-   System tests: This job will run system tests using pytest and tox.

Additionally, code quality checks will run during this stage, including Pylint and Mypy.

#### Deploy Stage

The Deploy stage is responsible for running deploy tests on the production environment. This stage will consist of the following job:

-   Deploy test: This job will deploy the package from the GitLab PyPi registry, install the package on all target production, and perform sanity tests (install and check version). This stage will also include performance testing and all tests with the decorator `@pytest.mark.deploy_test`.

#### Report Stage

The Report stage is responsible for generating a summary report for different information. This stage will consist of the following job:

-   Report: This job will generate a summary report that includes code quality, licenses used in the project, pipeline stats, artifacts available for download, performance information (if applicable), and information regarding the Python package, such as version, package size, and other statistics.

### Job Triggers

Each job can be triggered explicitly by setting the job name gitlab environmental variable. For example, the job `build-package` can be triggered by setting the variable `build_package = "ON"` in `.gitlab-ci.yml` variables or by pushing with the variable from git push `git push -o ci.variable="build_package=ON"`. All stages will be described under the configuration file located in `gitlab/gitlab.<JOB-NAME>.yml` and will be included from the main configuration file `.gitlab-ci.yml`.


## Tools

### Setup

This component provides setup for linting, testing, type-checking, validation, and documentation generation for the project.

### Tools Used

The following tools will be used:

-   pre-commit - responsible for git hooks. The configuration will be under project root `.pre-commit-config.yml` and will include different tools for code formatting and validations
-   linter - `pylint` with `.pylintrc` configuration file and `mypy` for type checking
-   `tox` - used for deployment and testing, configuration file is located in `tox.ini`
-   `coverage` - used with `pytest` for test coverage
-   `sphinx` - used for document generation
-   `pip-licenses` - used for license check
-   `flake8` - used for formatting
-   `setuptools_scm` - used for versioning strategy.


--------------------------------------------------------
# Design Document for Python Project Template

## Introduction
This design document outlines the architecture and implementation details for a Python project template. The template will provide a simple and fast way to deploy a Python project with a basic setup, including tools and Continuous Integration/Continuous Deployment (CI/CD) support. The primary goal of this project is to save time setting up new projects by providing a single point for change where best practices and new tools can be introduced and applied to all feature projects. This document provides an overview of the system, including its functional and non-functional requirements, constraints, dependencies, and risks. It is intended to guide the implementation and development of the system to meet the desired goals.

## System Architecture and Design

Free Text:

### project template
The project template will be generated based on the library [cookiecutter](https://github.com/cookiecutter/cookiecutter). This requires the user to have cookiecutter installed (`pip install --user cookiecutter`) or use the `pln-cli` tool.
	* `cookicutter` is used to generate template projects based on [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) and has a lot of [template projects](https://github.com/search?q=cookiecutter&type=Repositories) available on github. The `pln-proj-template` template will be located in github seeing that cookiecutter is built on top of github templates. cookiecutter receive user input and replace placeholder names in the template with the user supplied input.
	* To use template directly, user can install cookiecutter and run the following command and will be prompt for for the project name and other metadata
	  ```bash
cookiecutter gh:perchick03/perchick03/pln-proj-template-py
```

	* The directory structure required by cookiecutter looks as followed:
```text
pln-proj-template-pln/
├── {{ cookiecutter.project_name }}/  <--------- Project template
│   └── ...
├── blah.txt                      <--------- Non-templated files/dirs
│                                            go outside
│
└── cookiecutter.json             <--------- Prompts & default values
```

The output for project named `template-proj-demo` will be
```text
template-proj-demo/  <---------- Project name given by the user
│
└── ...       <-------- Files corresponding to those in your
                        cookiecutter's `{{ cookiecutter.project_name }}/` dir
```
### Project Filesystem Layout
- The filesystem layout for python project is chosen to be flat layout. `src layout` was also considered but for simplicity reasons, I chose flat layout which I have more experience with. Here is an example for src and flat layout for `awesome_package`  project
```text
# Src Layout
.
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── src/
│    └── awesome_package/
│       ├── __init__.py
│       └── module.py

# Flat Layout
.
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── awesome_package/
│   ├── __init__.py
│   └── module.py
```


| Layout      | Pros                                            | Cons                                                    |
| ----------- | ----------------------------------------------- | ------------------------------------------------------- |
| src-layout  | Clear separation of source code and other files | More complex file structure                             |
|             | Easier to navigate and find specific files      | May require additional setup (install in editable mode) |
|             | Encourages modular design                       | more difficult to understand for new developers         |
|             | Testing is done on installed package            |                                                         |
| ------      | -----------                                     | ------------------------                                |
| flat-layout | Simple and easy to understand                   | May become disorganized as the project grows            |
|             | No additional setup required                    | Difficult to find specific files                        |
|             | Files are easily accessible                     | Harder to enforce modular design                        |
* Testing will be organized in system, integration and unit test folders

### Generated Project Building
- This component will enable the generated project to be built into a valid Python wheel (`.whl`) package and `sdist` package.
- The build system chosen is setuptools. poetry was also considered but for simplicity, setuptools is used and in the future, I might migrate to poetry
- All information regarding the project metadata and build information will be stored in `pyproject.toml`. `setup.py` was also considered but it is deprecated and the community is moving toward setting `pyproject.toml` as the standard.
- to build a wheel, user can run `python3 build wheel sdist` from generated project root (where `pyproject.toml` is located )

### Versioning Strategy
* The version will be semantic version (MAJOR.MINOR.PATCH) using single sourcing for package version
* [setuptools-scm](https://pypi.org/project/setuptools-scm/) will be used for versioning. This assumes that the user is using the project over git
	* The tool will automatically use the correct version based on git tag

### Dependency Management
This component will ensure that project dependencies are included for production and development separately.
in the project root we will the dependencies into `requirements.txt` and `requirements-dev.txt` for development. in `pyproject.toml` the dependencies will be generated dynamically with
```toml
[tool.setuptools.dynamic]
dependencies = {file = ["requirements.txt"]}
```


### Python Entry Point Script
- This component will provide a simple CLI entry point script for the generated project. When a project is installed, an entry point cli will be available with `<project_name>_cli` command with the following flags
	- `--help` - show help message
	- `--version` - show package version
	- `--run-test` - run package tests (available only in development)
-
## GitLab
### registry
PyPi registry will be used by default for newly created packages in CICD. The package will be pushed automatically to gitalb PyPi when a new tag will be pushed.
Additionally, Gitlab docker registry will be used to store GitLab development image

### CICD Pipeline Setup
- This component will provide the necessary setup for continuous integration and deployment of the generated project.
- The project will have GitLab CICD pipeline. Github action, or other CICD may be used in the future
- each stage will be described under the configuration file located in `gitlab/gitlab.<JOB-NAME>.yml` and will be included from the main configuration file `.gitlab-ci.yml`
- Each job can be triggered explicitly by setting the job name gitlab environmental variable. For example, job `build-package`  can be triggered by setting the variable `build_package = "ON"` in `.gitlab-ci.yml` variables or by pushing with the variable from git push `git push -o ci.variable="build_package=ON"`
- The pipeline stages will be
	- Build - Build project artifact and validate them
		- GitLab development docker image build - Will be triggered on each change to `gitlab/Dockerfile.dev`, changes to `requirements-dev.txt` or if explicitly triggered
		- wheel, sdist package - will build, validates and upload gitlab registry
			- On git tag change, will also push artifacts to registry
		- documentation - Each merge to master, project documentation will be generated
	- Test - Run tests on project
		- Tests are split into unit, integration and system test, each with their own job
		- Tests will be run using pytest and tox
		- Linting - code quality checks will run during this stage. Pylint and mypy will be used
	- Deploy - Run deploy test on production environment
		- During this stage, we will deploy package from registry, install package on all target production and performe sanity test (install and check version)
		- This stage will include performance testing
		-
		- This stage will include all tests with the decorator `@pytest.mark.deploy_test`
	- Report - Generate summary report for different information
		- Code Quality - Pylint score, mypy errors, changes between target branch and current branch and code coverage.
		- license - what licenses are used in the project using `pip-licenses` tool
		- Pipeline stats - stats regarding the CICD pipeline
		- artifacts - All pipeline artifacts will be available for download here
		- Performance - If performance tests ran, will generate performance report
		- package - Information regarding python package such as version, package size and other stats

### Tools Setup
- This component will provide setup for linting, testing, type-checking, validation, and documentation generation
- Tools to be used
	- pre-commit - responsible for git hooks. The configuration will be under project root `.pre-commit-config.yml` and will include different tools for code formatting and validations
	- linter - using `pylint` with `.pylintrc` configuration file and `mypy` for type checking
	- `tox` - used for deployment and testing, configuration file is located in `tox.ini`
	- `coverage` - used with pytest for test coverage
	- `sphinx` - used for document generation
	- `pip-licenses` - used for license check
	- `flake8` - used for formatting
	- `setuptools_scm` - used fro versioning strategy
	-


The system will consist of the following components:



1. **Command Line Interface (CLI)** - This component will be responsible for accepting user inputs and deploying the new project based on the project template.

2. **Project Template** - This component will provide the basic setup for a Python project, including tools and CICD. It will be a single point for change and will ensure that all new projects benefit from updated tools and practices.

3. **Project Filesystem Layout** - This component will provide a well-organized layout for the generated project, based on best Python project practices.

4. **Project Building** - This component will enable the generated project to be built into a valid Python wheel (`.whl`) package and `sdist` package.

5. **Versioning Strategy** - This component will ensure that a well-defined versioning strategy is used for the generated project.

6. **Dependency Management** - This component will ensure that project dependencies are included for production and development separately.

7. **Python Entry Point Script** - This component will provide a simple CLI entry point script for the generated project.

8. **CICD Pipeline Setup** - This component will provide the necessary setup for continuous integration and deployment of the generated project.

9. **Tools Setup** - This component will provide setup for linting, testing, type-checking, validation, and documentation generation.

---------------------
