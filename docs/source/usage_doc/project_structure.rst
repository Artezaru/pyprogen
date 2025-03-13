Project structure
=================

Structure
-----------------

Once you have created a new project using the CLI (see the :doc:`quick_start` section), the project will have the following structure:

.. code-block:: console

   pyprogen
    ├── pyprogen
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── __version__.py
    |   └── ressources
    |        └── __init__.py
    ├── tests
    │   └── __init__.py
    ├── examples
    │   └── example.py
    ├── laboratory
    │   └── laboratory.py
    ├── venv
    ├── docs
    │   ├── source
    │   │   ├── conf.py
    │   │   ├── index.rst
    │   │   ├── installation.rst
    │   │   ├── usage.rst
    │   │   └── api.rst
    │   └── build
    │       ├── html
    │       └── latex
    ├── .github
    │   └── workflows
    │       └── sphinx.yml
    ├── README.md
    ├── LICENSE
    ├── Makefile
    ├── requirements.txt
    ├── pyproject.toml
    ├── .bumpver.toml
    ├── .gitlab-ci.yml
    └── .gitignore



Project Components
------------------

pyprogen
~~~~~~~~

The **pyprogen** directory is the main package of the project.

- ``__init__.py`` — Initializes the package.  
- ``__main__.py`` — Entry point if the package is executed directly.  
- ``__version__.py`` — Contains the package version information.  

.. note::

   To correctly add new modules, refer to the :doc:`create_module` section.

ressources
~~~~~~~~~~

The **ressources** directory contains additional resources for the package.

tests
~~~~~

The **tests** directory contains unit tests for the project, ensuring code correctness and reliability.
The module ``pytest`` is installed to run the tests.

examples
~~~~~~~~

The **examples** directory includes practical examples demonstrating how to use the package.

laboratory
~~~~~~~~~~

A **sandbox environment** for experiments and feature testing.

.. warning::

   This folder is **not versioned** by Git. It serves as a local space for testing new features and prototypes.

venv
~~~~

The **venv** directory contains the project's virtual environment.

.. note::

   To activate the virtual environment, see the :doc:`managing_venv` section.

docs
~~~~

The **docs** directory holds the project’s documentation.

- **source/** — Sphinx source files.  
- ``conf.py`` — Sphinx configuration file.  
- ``index.rst`` — Main documentation index.  
- ``api.rst`` — API reference.  
- ``usage.rst`` — Usage instructions.  
- ``installation.rst`` — Installation guide.
- **build/** — Generated documentation output.

.. note::

   To add or update the documentation, refer to the :doc:`generating_doc` section.

Other Files
-----------

.gitignore
~~~~~~~~~~

Specifies files and directories that Git should ignore.

README.md
~~~~~~~~~

Provides a general overview and description of the project.

requirements.txt
~~~~~~~~~~~~~~~~

Lists all the dependencies required by the project.

Makefile
~~~~~~~~

Contains commands to build and manage the project.

The available commands are:

- **help** — Show the available commands.
- **html** — Generate HTML documentation with Sphinx.
- **latexpdf** — Generate LaTeX PDF documentation with Sphinx.
- **clean** — Clean the documentation build directory.
- **bump** — Update the package version.
- **git** — Commit and push changes to the master branch.
- **app** — Build the application with PyInstaller.
- **test** — Run the tests with pytest.

LICENSE
~~~~~~~

Specifies the terms under which the project is licensed.

pyproject.toml
~~~~~~~~~~~~~~

Defines the project's metadata and dependencies to install the package.

.bumpver.toml
~~~~~~~~~~~~~

Contains the configuration for the version bumping process.

.gitlab-ci.yml
~~~~~~~~~~~~~~

Configuration file for GitLab CI/CD.

.github/workflows/sphinx.yml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration file for GitHub Actions.

