Project Structure
=================

Once you have created a new project by the CLI, (see :doc:`quick_start` section), the project will have the following structure:

.. code-block:: console

    .
    ├── pyprogen
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── __version__.py
    │   ├── ressources
    │   │   ├── __init__.py
    ├── tests
    ├── examples
    ├── laboratory
    ├── venv
    ├── docs
    │   ├── source
    │   │   ├── api_doc
    │   │   ├── usage_doc
    |   |   ├── conf.py
    |   |   ├── index.rst
    |   |   ├── api.rst
    |   |   ├── usage.rst
    |   ├── build
    ├── .github
    ├── ├── workflows
    ├── |   ├── documentation.yml
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    ├── Makefile
    └── LICENSE

The project structure is composed of the following directories and files:

- **pyprogen**: The main package of the project. To correctly add new modules, refer to the :doc:`write_module` section.
- **tests**: The directory containing the tests of the project.
- **examples**: The directory containing examples of how to use the package.
- **laboratory**: The directory containing the experiments and tests of the project. This folder is not versioned by git. It is a sandbox to test new features.
- **venv**: The virtual environment of the project. To activate the virtual environment, refer to the :doc:`activate_venv` section.
- **docs**: The directory containing the documentation of the project. To add new documentation, refer to the :doc:`write_documentation` section.
- **.gitignore**: The file containing the files and directories to ignore by git.
- **README.md**: The file containing the description of the project.
- **requirements.txt**: The file containing the dependencies of the project.
- **setup.py**: The file containing the metadata of the project.
- **Makefile**: The file containing the commands to build the project.
- **LICENSE**: The file containing the license of the project.