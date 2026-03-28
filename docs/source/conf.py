# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fasta Reader'
copyright = '2026, Ivan Alferov'
author = 'Ivan Alferov'
release = 'beta-01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    'sphinx.ext.autodoc',      # Автоматическое извлечение докстрингов
    'sphinx.ext.napoleon',     # Поддержка Google/NumPy style
    'sphinx.ext.viewcode',     # Добавление ссылок на исходный код
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_theme_options = {
    "color_mode": "dark", 
    "accent_color": "gold", 
}
html_static_path = ['_static']
