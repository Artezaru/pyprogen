Create a Command for Your Package
=================================

``pyprogen`` creates two commands for your package:

- ``<package_name>``: This command is used to run the package.
- ``<package_name>-gui``: This command is used to run the package with a graphical user interface (GUI).

For example, if your package name is ``mypackage``, the commands will be:

.. code-block:: bash

    mypackage
    mypackage-gui

These commands run the functions in the ``__main__.py`` file. By default, a NotImplementedError is raised, but you can customize the behavior by adding your code to the ``__main__.py`` file.

For example, let's configure our package to run the ``addition`` function for 1 + 2 when the command is executed.

1. Open the ``__main__.py`` file in the package directory.

2. Add the following code:

.. code-block:: python

    from .addition import addition

    def __main__():
        print(addition(1, 2))
    
    def __main_gui__():
        raise NotImplementedError("The GUI is not implemented yet.")

Now when you run the command ``mypackage``, the output will be:

.. code-block:: bash

    (venv) user@host:~/project$ mypackage
    3

.. note::

    If the command will open a GUI, you can add the code to the ``__main_gui__`` function.
    It is recommended to use the ``__main__`` function for the command and the ``__main_gui__`` function for the GUI command because Windows does not have the same behavior as Unix systems when running the GUI command.
    If a GUI is open with ``__main__``, the GUI can fail on Windows systems.

.. note::

    To simplify the package, please only call some functions in the ``__main__`` and ``__main_gui__`` functions, but do not add the entire code in these functions.
    It will be easier to test and maintain the package.
