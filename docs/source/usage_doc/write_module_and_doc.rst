Write Modules and Documentation
===============================

This guide explains how to create new modules and document them using **Sphinx** with **Numpydoc** style.

Before starting, ensure that you have:

- Created a new project (see :doc:`quick_start`)  
- Activated the virtual environment (see :doc:`activate_venv`)

Writing Modules
---------------

To add new functionality, create Python files inside your package directory (e.g., `<package>/`) and document them using **Numpydoc** style.

### Example: Adding a Function

1. **Create** a file (e.g., `add.py`) and define your function:

.. code-block:: python

    def add(a: int, b: int) -> int:
        r"""
        Add two integers.

        Parameters
        ----------
        a : int
            First number to add.
        b : int
            Second number to add.

        Returns
        -------
        int
            Sum of the two numbers.

        Raises
        ------
        ValueError
            If either input is not an integer.

        Examples
        --------
        >>> add(2, 3)
        5
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Inputs must be integers.")
        return a + b

2. **Expose** the function in `__init__.py`:

.. code-block:: python

    from .add import add

    __all__ = ["add"]

### Using Relative Imports

When importing functions from other modules within your package, use **relative imports**. For example, if `add.py` needs to import `multiply` from `multiply.py`:

.. code-block:: python

    from .multiply import multiply

Writing Documentation
---------------------

Use **Sphinx** and **Numpydoc** to document your project. The project is pre-configured to support:

- **Autodoc** for generating documentation from docstrings.
- **Numpydoc** for parsing Numpy-style docstrings.
- **LaTeX** rendering for math equations.

> See [Sphinx Docs](https://www.sphinx-doc.org/en/master/) and [Numpydoc Docs](https://numpydoc.readthedocs.io/en/latest/format.html) for more details.

### Documenting Functions

1. **Create an `.rst` file** in `docs/source/api_doc/` for each module. Example for `add.py`:

.. code-block:: rst

    add
    ===

    .. autofunction:: <package_name>.add

2. **Update the API Reference** in `docs/source/api.rst`:

.. code-block:: rst

    API Reference
    =============

    .. toctree::
        :maxdepth: 1

        ./api_doc/add

Building the Documentation
--------------------------

1. **Activate** the virtual environment.
2. **Build** the HTML documentation:

.. code-block:: console

    make html

3. Open the documentation:

.. code-block:: console

    docs/build/html/index.html

Best Practices
--------------

- Use **Numpydoc** format for all docstrings.
- Write **clear examples** and document **edge cases**.
- Use **relative imports** within the package.
- Keep the **API reference** updated after adding modules.
- Exclude the `venv/` directory from version control.

Next Steps
----------

To learn more about **building documentation** and pushing to **GitHub**, see the :doc:`use_git` section.
