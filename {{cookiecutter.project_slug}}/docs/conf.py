# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

import {{ cookiecutter.project_slug }}

project = '{{ cookiecutter.project_name }}'
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"

# The short X.Y version.
version = {{ cookiecutter.project_slug }}.__version__
# The full version, including alpha/beta/rc tags.
release = {{ cookiecutter.project_slug }}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'

# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     '{{ cookiecutter.project_name }} Documentation',
     [author], 1)
]
