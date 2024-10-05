"""Sphinx configuration file for AutoGen using Sphinx Awesome Theme."""

from __future__ import annotations

from dataclasses import asdict
import sys
from typing import Any, Dict
from pathlib import Path

from sphinx.application import Sphinx
from sphinxawesome_theme import ThemeOptions, __version__
from sphinxawesome_theme.postprocess import Icons
from sphinx.util.docfields import Field

# -- Project information -----------------------------------------------------
project = "autogen_core"
author = "Microsoft"
copyright = f"2024, {author}"
version = "0.2"

sys.path.append(str(Path(".").resolve()))
# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx_design",
    # "sphinx_copybutton",
    "_extension.gallery_directive",
    "myst_nb",
]

suppress_warnings = ["myst.header"]
napoleon_custom_sections = [("Returns", "params_style")]
templates_path = ["_templates"]
autoclass_content = "init"

# TODO: include all notebooks excluding those requiring remote API access.
nb_execution_mode = "off"
nb_execution_raise_on_error = True
nb_execution_timeout = 60

myst_heading_anchors = 5
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "strikethrough",
]


# -- Options for HTML output -------------------------------------------------
html_title = "AutoGen"
html_theme = "sphinxawesome_theme"
html_static_path = ["_static"]
html_css_files = [
    "custom.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"]
html_js_files = [""]


#  "display_github": True, # Integrate GitHub
#     "github_user": "MyUserName", # Username
#     "github_repo": "MyDoc", # Repo name
#     "github_version": "master", # Version
#     "conf_py_path": "/source/", # Path in the checkout to the docs root

html_baseurl = "/autogen/dev/"
announcement = '<span class="fa-solid fa-triangle-exclamation"></span> AutoGen v0.4 is a work in progress. Go <a href="/autogen/0.2/">here</a> to continue using v0.2 documentation.'
html_context = {
    'display_github': True,
    "github_user": "microsoft",
    "github_repo": "autogen",
    "github_version": "main",
    "doc_path": "python/packages/autogen-core/docs/src/",
    "conf_py_path": "python/packages/autogen-core/docs/src/",
    'theme_announcement': announcement,
}

pygments_style = "sphinx"

html_permalinks_icon = Icons.permalinks_icon

# Select theme for both light and dark mode
# pygments_style = "color"
# Select a different theme for dark mode
# pygments_style_dark = "PYGMENTS_THEME"

theme_options = ThemeOptions(
    show_prev_next=False,
    awesome_external_links=True,
    main_nav_links={
        "AgentChat": "/agentchat-user-guide/index",
        "Core": "/core-user-guide/index",
        "Packages": "/packages/index",
        "API Reference": "/reference/index",
    },
    extra_header_link_icons={
        "Twitter": {
            "link": "https://twitter.com/pyautogen",
            "icon": (
                '<svg height="22px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 512 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"/>'
                '</svg>'
            ),
        },
        "GitHub": {
            "link": "https://github.com/microsoft/agnext",
            "icon": (
                '<svg height="22px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                '14.853 20.608 1.087.2 1.483-.47 1.483-1.047 0-.516-.019-1.881-.03-3.693-6.04 '
                '1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 '
                '2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 1.803.197-1.403.759-2.36 '
                '1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 '
                '1.822-.584 5.972 2.226 1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 '
                '4.147-2.81 5.967-2.226 5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 '
                '2.232 5.828 0 8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 '
                '2.904-.027 5.247-.027 5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 '
                '22.647c0-11.996-9.726-21.72-21.722-21.72" fill="currentColor"/>'
                '</svg>'
            ),
        },
        # "PyPI": {
        #     "link": "/packages",
        #     "icon": (
        #         '<svg height="26px" style="margin-top:-2px;display:inline" '
        #         'viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
        #         '<path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm-1.6 20.8v-3.2H6.8v-1.6h3.6v-3.2H6.8V11h3.6V6.8h-6v14h6zm9.6-9.6h-3.6v3.2h3.6v1.6h-3.6v3.2h-1.6v-14h5.2v6z"/>'
        #         '</svg>'
        #     ),
        # },
    },

)


html_theme_options = asdict(theme_options)

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}


# def setup_to_main(
#     app: Sphinx, pagename: str, templatename: str, context, doctree
# ) -> None:
#     """Add a function that jinja can access for returning an "edit this page" link pointing to `main`."""

#     def to_main(link: str) -> str:
#         """Transform "edit on github" links and make sure they always point to the main branch.

#         Args:
#             link: the link to the github edit interface

#         Returns:
#             the link to the tip of the main branch for the same file
#         """
#         links = link.split("/")
#         idx = links.index("edit")
#         return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2:])

#     context["to_main"] = to_main


def setup(app: Sphinx) -> None:
    """Register the ``confval`` role and directive.

    This allows to declare theme options as their own object
    for styling and cross-referencing.
    """
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )
