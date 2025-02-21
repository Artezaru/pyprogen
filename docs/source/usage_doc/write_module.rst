Write modules
=============

Once you have created a new project by the CLI, (see :doc:`quick_start` section) and activated the virtual environment (see :doc:`activate_venv` section), you can add new modules to your package.

To add a new class or function to the package, create a new Python file in the ``<package>`` directory named ``<function>.py``. Then, add the following code to the file:

.. code-block:: python

    def <function>(<parameters>):
        """<docstring>"""
        <code>

Then go to the ``__init__.py`` file in the ``<package>`` directory and add the following line:

.. code-block:: python

    from .<function> import <function>

    __all__ = [
        "<function>",
    ]

This line will import the new module in the package and make it available to the user.

If the ``<function>.py`` need to import other classes or functions from the package, must use local imports. For example, to import the ``<class>`` class from the ``<class>.py`` file, use the following code:

.. code-block:: python

    from .<class> import <class>

To learn how to write the documentation files, refer to the :doc:`write_documentation` section.
