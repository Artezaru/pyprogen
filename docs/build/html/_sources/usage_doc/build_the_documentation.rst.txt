Build the documentation
=======================

Once you have written the documentation of the package (see :doc:`write_documentation` section), you can build the documentation by running the following command in the root directory of the project:

.. code-block:: console

    make html

This command will build the documentation in the ``docs/build`` directory. To see the documentation, open the ``index.html`` file in your browser.

Sphinx can also generate a Latex document by running the following command:

.. code-block:: console

    make latexpdf

.. note::

    The documentation is built using Sphinx. Make sure you have installed Sphinx in your virtual environment before running the command.
    If Sphinx is not installed, you can install it by running the following command:

    .. code-block:: console

        pip install sphinx
        pip install pydata_sphinx_theme

    To activate the virtual environment, refer to the :doc:`activate_venv` section.

