Write Documentation
===================

Once you have created a new project by the CLI, (see :doc:`quick_start` section) and activated the virtual environment (see :doc:`activate_venv` section), you can start writing the documentation of your project.

By using sphinx and reStructuredText, you can write the documentation of your project in a structured way. To learn more about the syntax of reStructuredText, refer to the `reStructuredText Directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_.

The project is set to be able reading Latex math equations and to use the autodoc extension. This extension allows you to automatically generate the documentation of your modules and classes.
See the Sphinx documentation for more information (https://www.sphinx-doc.org/en/master/contents.html).

An example of a documented function is shown below:

.. code-block:: python

    def add(a: int, b: int) -> int:
        r"""
        This function adds two numbers together.

        .. warning::
            
            The 'r' before the triple quotes allows to write a raw string.

        .. math::
            
            a + b = c \text{ where } a, b, c \in \mathbb{Z}

        Parameters
        ==========
        a : int
            The first number to add.
        b : int
            The second number to add.

        Returns
        =======
        int
            The sum of the two numbers.

        Example
        =======
        >>> add(1, 2)
        3

        Raises
        ======
        ValueError
            If the parameters are not integers.
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("The parameters must be integers.")
        return a + b

Once a function is documented, go to the ``docs/source/api_doc`` directory and create a new file named ``add.rst``. Then, add the following code to the file:

.. code-block:: rst

    add
    ===

    .. autofunction:: <package_name>.add

See the autodoc documentation for more information (https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html).

Then go to the ``docs/source/api.rst`` file and add the following code:

.. code-block:: rst

    .. toctree::
        :maxdepth: 1

        ./api_doc/add

This line will add the new function to the API reference.

