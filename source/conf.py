# Configuration file for the Sphinx documentation builder.

import os
import sys

# Allow Sphinx to find your project source code (IMPORTANT)
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'PiXELL-River Financial System'
copyright = '2025, Kamaldeep Kaur'
author = 'Kamaldeep Kaur'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc'   # This generates documentation from docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
