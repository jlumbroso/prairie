# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

project = "prairie"
copyright = "2023–{}, Jérémie Lumbroso".format(datetime.datetime.now().year).replace("2023–2023", "2023")
author = "Jérémie Lumbroso"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
try:
    import prairie
    version = '.'.join(map(str, prairie.version_info[:2]))
    release = prairie.__version__
except ImportError:
    version = ''
    release = ''

# Censor sensitive information before generating the docs
# try:
#     import prairie.slack.clients
#     prairie.slack.clients.SLACK_TOKEN = "<SLACK TOKEN>"
# except ImportError:
#     pass


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Autodoc Type Hints turned on (beta in 2.4, core in 3.x)
autodoc_typehints = "description"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    "style_nav_header_background": "#6DB154",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
