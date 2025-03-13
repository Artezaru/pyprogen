Writing and Generating Documentation for the Project
====================================================

To write the documentation for the project, you can use the reStructuredText (RST) format. RST is a lightweight markup language that is easy to read and write. It is commonly used in the Python community for writing documentation.

Generating the documentation is a multi-step process that involves writing the documentation, organizing it into sections, and generating the HTML output.

Writing the Documentation
-------------------------

Let's consider the ``addition`` and ``subtraction`` functions that we created in the previous sections. We want to document these functions so that other developers can understand how to use them.

``pyprogen`` package is configured to use the Numpy style docstrings. This style is based on the Numpy documentation and is widely used in the Python community.

To document a function, you need to add a docstring to the function definition. The docstring should describe what the function does, what arguments it takes, and what it returns. 
We recommend using a raw string (r-string) to write the docstring. This will allow you to write the docstring on multiple lines without having to use the escape character ``\``. Furthermore, this will enable you to use environments such as the ``:math:`` environment to write mathematical equations in LaTeX.

For example, to document the ``addition`` function, you can add the following docstring:

.. code-block:: python

    def addition(a: int, b: int) -> int:
        r"""
        Add two numbers together.

        The numbers are noted :math:`a` and :math:`b`.

        .. math::

            a + b
        
        .. code-block:: python

            addition(1, 2)
            3
        
        .. warning::

            Only give 2 numbers as arguments.

        Parameters
        ----------
        a : int
            The first number to add.
        b : int
            The second number to add.

        Returns
        -------
        int
            The sum of the two numbers.
        """
        return a + b

.. note::

    The docstring is enclosed in triple quotes (``"""``) to indicate that it is a multi-line string and the "r" before the first quote is to indicate that it is a raw string.

With Numpy style docstrings, the docstring is divided into sections:

- The first line is a short description of the function.
- **Jump one line**
- The next lines provide a more detailed description of the function.
- **Jump one line**
- The ``Parameters`` section lists the arguments that the function takes, along with their types and descriptions.
- The ``Returns`` section describes what the function returns.
- The ``Raises`` section lists the exceptions that the function can raise.
- The ``Examples`` section provides examples of how to use the function.

For each section, you must underline the title with the same number of characters as the title. For example, the title ``Parameters`` is underlined with 10 characters '-'.

The input parameters are described with the following syntax:

.. code-block:: python

    parameter_name : parameter_type
        Description of the parameter.
    
The return value is described with the following syntax:

.. code-block:: python

    return_type
        Description of the return value.


Adding reStructuredText Structures
----------------------------------

With Sphinx and reStructuredText, you can add various structures to your documentation, such as:

- Equations
- Code blocks
- Warnings
- Notes
- etc ...

To create a structure in reStructuredText, you need to use the appropriate directive. For example, to create a code block, you can use the ``code-block`` directive:

.. code-block:: rst

    .. code-block:: python

        def addition(a: int, b: int) -> int:
            return a + b

.. warning::

    You must use a tabulation to indent the code block. 
    You must add a blank line before and after the code block.

For more details on the reStructuredText syntax, you can refer to the `official documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.

Organizing the Documentation
----------------------------

Once the functions are documented, ``pyprogen`` is configured to use autodoc to automatically generate the documentation from the docstrings.

In the 'docs/source' directory, you can find the 'api.rst' file. This file is used to organize the documentation of the package.

Add the following content to the 'api.rst' file:

.. code-block:: rst

   .. toctree::
    :maxdepth: 1

    ./api_doc/addition
    ./api_doc/subtraction

This content will create a table of contents (TOC) that links to the documentation of the ``addition`` and ``subtraction`` functions.
This syntax indicates that the documentation of the functions is in the 'api_doc' directory under the names 'addition.rst' and 'subtraction.rst'.

Create the 'api_doc' directory in the 'docs/source' directory and add the 'addition.rst' and 'subtraction.rst' files.

In the 'addition.rst' file, add the following content:

.. code-block:: rst

    Addition Function
    =================

    .. autofunction:: pyprogen.addition
    
In the 'subtraction.rst' file, add the following content:

.. code-block:: rst

    Subtraction Function
    ====================

    .. autofunction:: pyprogen.subtraction

This is an example of how to organize the documentation of the functions. 
You can organize the documentation as you want by creating new directories and files, and you can add more details directly in the `.rst` files.
See the `official documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ for more details.

Generating the HTML Output
--------------------------

To generate the HTML output, the ``pyprogen`` package is configured to use Sphinx in the root directory of the project.

You can use the following command to generate the HTML output:

.. code-block:: bash

    make html

This command will generate the HTML output in the 'docs/build/html' directory.

If you want to clean the build directory before generating the HTML output, you can use the following command:

.. code-block:: bash

    make clean

To check if the documentation is correctly generated, open the 'docs/build/html/index.html' file in a web browser.

The documentation must be generated each time you update the documentation or the docstrings of the functions.

Pushing the Documentation to GitHub Pages or GitLab Pages
---------------------------------------------------------

To share the documentation with other developers, you can push the documentation to GitHub Pages or GitLab Pages.
The ``pyprogen`` package is configured to use workflows to automatically push the documentation to GitHub Pages or GitLab Pages.
See the section :doc:`git_and_push` for more details.
