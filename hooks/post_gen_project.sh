#!/bin/bash

# shellcheck disable=SC2050
if [[ "{{cookiecutter.init_project}}" == "no" ]]; then
  echo "Skipping project initialization..."
  exit 0
fi


function install_project() {
  # Create virtual environment if not already activated, otherwise use current
  if [[ "$VIRTUAL_ENV" == "" ]]; then
      echo "Creating virtual environment..."
      pip install virtualenv
      virtualenv venv
      # shellcheck disable=SC1091
      . venv/bin/activate
  else
      echo "Using current virtual environment $VIRTUAL_ENV..."
  fi

  pip install --upgrade pip

  # Install project editable
  echo "Installing project editable..."
  pip install -e .

  # Install dependencies
  echo "Installing dependencies..."
  pip install -r requirements_dev.txt
}


function initialize_local_project() {
  echo "Initializing {{cookiecutter.project_name}} project..."
  git init
  git add .

  # Install pre-commit hooks in background
  pre-commit install
  pre-commit autoupdate
  pre-commit run --all-files || true


  # TODO: pre-commit fails currently, add the changed files and commit.
  git add .
  git commit -m "Initial commit" --no-verify
}

initialize_local_project
install_project

# Skip gitlab initialization if not set to yes
if [[ "{{cookiecutter.init_gitlab}}" != "yes" ]]; then
  echo "removing gitlab initialization"
  rm -rf gitlab
  rm .gitlab-ci.yml
  echo "done initializing project {{cookiecutter.project_name}}"
  exit 0
fi


function initialize_gitlab_proj() {
  echo "Initializing {{cookiecutter.project_name}} project..."
  # Assume SSH key is already added to GitLab
  REMOTE_URL="git@{{cookiecutter.gitlab_url}}:{{cookiecutter.gitlab_namespace}}/{{cookiecutter.project_name}}.git"

  echo "Adding Gitlab remote project to $REMOTE_URL..."
  git remote add origin "$REMOTE_URL"

  # if gitlab remote project does not exist, create it
  if ! git ls-remote --exit-code --heads "$REMOTE_URL" master &> /dev/null; then
    # First push, only build CI/CD image, not need to run full pipeline
    git push --set-upstream "$REMOTE_URL" master -o ci.variable=build_ci_image=ON
    echo "Gitlab remote project initialized at $REMOTE_URL"
  else
    echo "Gitlab remote project already exists at $REMOTE_URL"
  fi
}

initialize_gitlab_proj
