# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "test"
copyright = "2025, Matheus"
author = "Matheus"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os  # noqa: E402
import sys  # noqa: E402

# Add the path to the directory containing your module
sys.path.insert(0, os.path.abspath("../../src/"))
extensions = ["sphinx.ext.autodoc", "myst_parser", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]


# --------------------------
# import os
# import sys
# # Add the path to the directory containing your module
# sys.path.insert(0, os.path.abspath('../../src/'))
