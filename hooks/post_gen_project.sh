#!/bin/bash

# shellcheck disable=SC2050
if [[ "{{cookiecutter.initialize_project}}" == "no" ]]; then
  echo "Skipping project initialization..."
  exit 0
fi

# Initialize git repository
echo "Initializing git repository..."
git init
git add .
git commit -m "Initial commit"

if [[ "$VIRTUAL_ENV" == "" ]]; then
    # Create virtual environment
    echo "Creating virtual environment..."
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
fi

# Install project editable
echo "Installing project editable..."
pip install -e .

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements_dev.txt

# Install pre-commit hooks in background
pre-commit install
pre-commit autoupdate