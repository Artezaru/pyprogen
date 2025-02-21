Project Structure
=================

Once you have created a new project using the CLI (see the :doc:`quick_start` section), the project will have the following structure:

.. code-block:: console

    .
    ├── pyprogen
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── __version__.py
    │   └── ressources
    │       └── __init__.py
    ├── tests
    ├── examples
    ├── laboratory
    ├── venv
    ├── docs
    │   ├── source
    │   │   ├── api_doc
    │   │   ├── usage_doc
    │   │   ├── conf.py
    │   │   ├── index.rst
    │   │   ├── api.rst
    │   │   └── usage.rst
    │   └── build
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    ├── Makefile
    └── LICENSE

Project Components
------------------

pyprogen
~~~~~~~~

The **pyprogen** directory is the main package of the project.

- ``__init__.py`` — Initializes the package.  
- ``__main__.py`` — Entry point if the package is executed directly.  
- ``__version__.py`` — Contains the package version information.  
- **ressources/** — Additional package resources.  
- ``__init__.py`` — Initializes the resources module.

.. note::

   To correctly add new modules, refer to the :doc:`write_module_and_doc` section.

tests
~~~~~

The **tests** directory contains unit tests for the project, ensuring code correctness and reliability.

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

   To activate the virtual environment, see the :doc:`activate_venv` section.

docs
~~~~

The **docs** directory holds the project’s documentation.

- **source/** — Sphinx source files.  
- **api_doc/** — API documentation.  
- **usage_doc/** — Usage guides.  
- ``conf.py`` — Sphinx configuration file.  
- ``index.rst`` — Main documentation index.  
- ``api.rst`` — API reference.  
- ``usage.rst`` — Usage instructions.  
- **build/** — Generated documentation output.

.. note::

   To add or update the documentation, refer to the :doc:`write_module_and_doc` section.

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

setup.py
~~~~~~~~

Defines the project’s metadata and setup configuration.

Makefile
~~~~~~~~

Contains commands to build and manage the project.

LICENSE
~~~~~~~

Specifies the terms under which the project is licensed.

