Adding Functions to the Package
===============================

To create a function within the package, you need to create a new module in the package directory. In this example, we will create two functions: ``addition`` and ``subtraction``.

The two functions can be placed in the same Python file, but for clarity, we will create two separate files. This will also introduce the concept of **relative imports**.

Creating the Addition Function
-------------------------------

In the package directory, create a new file named ``addition.py`` with the following content:

.. code-block:: python

    def addition(a: int, b: int) -> int:
        return a + b

To add the function to the package, you must import it in the ``__init__.py`` file. Open the ``__init__.py`` file and add the following line:

.. code-block:: python

    from .addition import addition

    __all__ = [
        ... # other functions, classes, or subpackages
        'addition'
    ]

The dot before the module name allows you to import the module from the same package (i.e., the same directory). This is called a **relative import**, and it is mandatory to use it when importing modules within the same package.

Now you can use the ``addition`` function anywhere in your package. For example, in the laboratory directory, create a new file named ``lab_addition.py`` with the following content:

.. code-block:: python

    from mypackage import addition

    print(addition(1, 2))

You will see that the function works correctly. If your package is not installed, you can install it in "editable" mode by running the following command in the root directory of the project:

.. code-block:: bash

    pip install -e .

The advantage of using packages with relative imports is that once the package is installed, you don't need to use sys.path.append or other methods to find the package. You can directly import the package and use the functions as if they were part of the standard library.

Creating the Subtraction Function
----------------------------------

Next, we want to add a new function that uses the ``addition`` function. Create a new file named ``subtraction.py`` in the package directory with the following content:

.. code-block:: python

    from .addition import addition

    def subtraction(a: int, b: int) -> int:
        return addition(a, -b)

The ``addition`` function is imported from the same package using a relative import.

Again, to add the function to the package, import it in the ``__init__.py`` file:

.. code-block:: python

    from .addition import addition
    from .subtraction import subtraction

    __all__ = [
        ... # other functions, classes, or subpackages
        'addition',
        'subtraction'
    ]

Running the Functions
----------------------

In a package, you cannot run a file directly. Instead, you must create a script that will call the function, such as the ``lab_addition.py`` file mentioned earlier. Create a new file named ``lab_subtraction.py`` in the laboratory directory with the following content:

.. code-block:: python

    from mypackage import subtraction

    print(subtraction(1, 2))

Documentation
-------------

To document the functions, please refer to the :doc:`generating_doc` section.
