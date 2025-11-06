# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# --- PATH CONFIGURATION FOR DJANGO AUTODOC (CRITICAL) ---

# This ensures the Sphinx builder can find your Django project modules
sys.path.insert(0, os.path.abspath('..'))
# Add your Django project settings directory to the path as well
sys.path.insert(0, os.path.abspath('../oc_lettings_site'))

# Configure Django settings for model/view access
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# --- PROJECT INFORMATION ---

project = 'Devogs-OC-lettings-FR'
copyright = '2025, Mathieu P.'
author = 'Mathieu P.'
release = '2.0'
version = '2.0'

# --- GENERAL CONFIGURATION ---

# Add any Sphinx extension module names here, as strings.
extensions = [
    # Required for reading Python docstrings
    'sphinx.ext.autodoc', 
    # Optional: Supports NumPy and Google style docstrings (recommended for clean code)
    'sphinx.ext.napoleon', 
    # Optional: Useful for linking between documentation pages and external sites
    'sphinx.ext.intersphinx', 
    # Allows you to link to the source code (e.g., GitHub)
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# --- HTML OUTPUT CONFIGURATION ---

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme' # Recommended theme for Read the Docs
html_static_path = ['_static']

# Ensure the 'source' directory is recognized (it is not explicitly needed here, 
# but good for clarity in the standard sphinx structure)
source_suffix = '.rst'
