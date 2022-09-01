# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PPSQL'
copyright = '2022, Python for PostgreSQL'
author = 'lc06'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
     'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    "sphinx_thebe",
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'myst_nb',
    'jupyter_sphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Allow errors
execution_allow_errors = True

# Do not execute cells
jupyter_execute_notebooks = "off"

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
