Running Tests Before Pushing the Code
-------------------------------------

Before pushing the code to the repository, it is a good practice to run the tests to ensure that the code is working correctly. 
By default, ``pyprogen`` allows the use of the ``pytest`` framework to run tests, but other frameworks can be used as well.

Let's consider the ``addition`` function created previously. 
To test this function, create a new file named ``test_addition.py`` in the ``tests`` directory with the following content:

.. code-block:: python

    from pyprogen import addition
    import pytest

    def test_addition():
        assert addition(1, 2) == 3
        assert addition(-1, 1) == 0
        assert addition(0, 0) == 0

Then, run the tests by executing the following command in the root directory of the project:

.. code-block:: bash

    pytest tests/

Alternatively, you can directly use the ``make`` command:

.. code-block:: bash

    make test

The output should show that all tests passed. If any test fails, you should fix the code before pushing it to the repository.

``pytest`` is a powerful framework that allows you to write tests in a simple and readable way. For more information, see the `official documentation <https://docs.pytest.org/en/stable/>`_.
