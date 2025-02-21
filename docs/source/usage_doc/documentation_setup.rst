Setting Manually the Documentation
==================================

If the documentation is not set up automatically, you can configure it manually by following these steps.

Folder Structure
----------------

As described in the :doc:`project_structure` section, begin by creating the following folder structure:

.. code-block:: console

    docs/
    ├── source/
    │   ├── api_doc/
    │   ├── usage_doc/
    │   ├── conf.py
    │   ├── index.rst
    │   ├── api.rst
    │   └── usage.rst
    └── build/
        └── html/

- **docs/** — The root directory for the documentation.
- **source/** — Contains the Sphinx source files.
- **api_doc/** — For API-related documentation.
- **usage_doc/** — For usage guides.
- ``conf.py`` — Sphinx configuration file.
- ``index.rst`` — Main documentation index.
- ``api.rst`` — API reference.
- ``usage.rst`` — Usage instructions.
- **build/** — The output directory for the built documentation.
- **html/** — The generated HTML files will be stored here.

In the root of the project (at the same level as the ``pyprogen`` package), add the ``Makefile`` to simplify the build process.

.. note::

   File templates can be found in the :doc:`../ressources` section.

Installing Dependencies
-----------------------

Activate your virtual environment and install the required Sphinx dependencies:

.. code-block:: console

    pip install sphinx
    pip install pydata_sphinx_theme

Building the Documentation
--------------------------

Once everything is set up, build the HTML documentation using the following command:

.. code-block:: console

    make html

The generated documentation will be available in the ``docs/build/html/`` directory.

To view it, open the following file in your web browser:

.. code-block:: console

    docs/build/html/index.html

Hosting Documentation on GitHub Pages
-------------------------------------

If you want to host the documentation on **GitHub Pages**, follow these steps:

1. Initialize a new branch named **gh-pages** in your Git repository.
2. Push the contents of the ``docs/build/html/`` folder to the **gh-pages** branch.

Refer to the :doc:`git_setup` section for detailed instructions on setting up Git for your project.

.. note::

   Hosting your documentation on **GitHub Pages** allows it to be publicly accessible through a GitHub-hosted URL.
