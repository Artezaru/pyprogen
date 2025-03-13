Managing virtual environments
=============================

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a specific project without affecting other projects or the system's Python installation.


Activation
----------

To activate the virtual environment, go to the project's root directory and run the following commands:

.. code-block:: bash

    cd /path/to/your/project
    source venv/bin/activate

To ensure that the virtual environment is activated, the command prompt will change to show "(venv)" at the beginning of the line.
You can also check the Python by running the following command:

.. code-block:: bash

    which python

The output should point to the Python executable inside the virtual environment. Otherwise, the virtual environment is not correctly activated.

To deactivate the virtual environment, run the following command:

.. code-block:: bash

    deactivate


Install packages
----------------

Once the virtual environment is activated, you can install packages using the ``pip`` command. For example, to install the package ``requests``, run the following command:

.. code-block:: bash

    pip install requests

To install packages from a git repository, run the following command:

.. code-block:: bash

    pip install git+https://github.com/<username>/<repository>.git

To see installed packages, run the following command:

.. code-block:: bash

    pip freeze
