# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


copyright = '2024, Haptikos'
author = 'Haptikos'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/Haptikos.png"
html_title = "Haptikos Documentation"
html_css_files = ['custom.css']
master_doc = 'index'
html_theme_options = {
    "sidebar_hide_name": False,  # Ensure project name is visible in sidebar
    "navigation_with_keys": True,  # Allow keyboard navigation
}