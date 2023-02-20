# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# Example fo conf.py file: https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/docs/conf.py
import os
import sys
import traceback
from importlib.metadata import version

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../../'))


project = '{{cookiecutter.project_name}}'
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = '{{cookiecutter.full_name}}'
try:
    release = version('{{cookiecutter.project_name}}')
except Exception:
    traceback.print_exc()
    release = '0.0.1'

# for example take major/minor
version = '.'.join(release.split('.')[:2])

# Include .ini files in the Sphinx source parser
source_parsers = {
    '.ini': 'sphinxcontrib.ini.rst_ini_parser',
}

# Define a mapping for the .ini file extension
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.ini': 'ini',
}

# Add any additional extensions you need
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.ini',
]


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
