Install Packages
================

Once you have created a new project by the CLI, (see :doc:`quick_start` section) and activated the virtual environment (see :doc:`activate_venv` section), you can install new packages to your project.

.. seealso::

    Also, to learn how to install a package, refer to the `Python Packaging User Guide <https://packaging.python.org/>`_.
    A short guide is available below for the most common commands.

To install a new package from the Python Package Index (PyPI), run the following command:

.. code-block:: console

    pip install <package_name>

If your ``requirements.txt`` file is up-to-date, you can install all the packages listed in the file by running the following command:

.. code-block:: console

    pip install -r requirements.txt

To install a package from a Github repository, run the following command:

.. code-block:: console

    pip install git+https://github.com/<username>/<repository>.git

To see the list of installed packages, run the following command:

.. code-block:: console

    pip freeze

In order to test your package before publishing it, you can install it locally by running the following command in the root of the project:

.. code-block:: console

    pip install -e .

This command will install the package in editable mode, meaning that you can modify the code and see the changes directly in the package.
Then you can write your tests and examples in the ``tests`` and ``examples`` directories respectively using the package you just installed.

.. code-block:: python

    import <package_name>

To correctly add new modules to the package, refer to the :doc:`write_module`.