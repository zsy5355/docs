# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from typing import Union
from unittest.mock import MagicMock
import sys

# Mock modules that are not available on Read the Docs
MOCK_MODULES = ['recommonmark', 'sphinx_markdown_tables']
sys.modules.update((mod_name, MagicMock()) for mod_name in MOCK_MODULES)
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode', 'recommonmark', 'sphinx_markdown_tables']


project = 'docs'
copyright = '2023, zs'
author = 'zs'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = [
#        'recommonmark',
#        'sphinx_markdown_tables'
#        ]



templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
