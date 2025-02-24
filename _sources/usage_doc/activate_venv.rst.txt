Using Virtual Environments
==========================

Virtual environments (**venv**) help isolate project dependencies, ensuring that each project uses the correct versions of packages without conflicts.

Creating a Virtual Environment
------------------------------

To create a new virtual environment in your project, navigate to the **root** of the project and run the following command:

.. code-block:: console

    python -m venv venv

The virtual environment package ``virtualenv`` can be used as an alternative to the built-in ``venv`` module:

.. code-block:: console

    pip install virtualenv
    virtualenv venv

This will create a new directory named **`venv`** containing the isolated Python environment.

- **`venv/`** — The directory that holds the virtual environment.  
- **`Scripts/`** (Windows) or **`bin/`** (Unix) — Contains activation scripts and executables.




Activating the Virtual Environment
----------------------------------

To start using the virtual environment, you need to **activate** it.

**On Windows:**

.. code-block:: console

    venv\Scripts\activate.bat

Or, if you're using **PowerShell**:

.. code-block:: console

    venv\Scripts\Activate.ps1

**On Unix/MacOS:**

.. code-block:: console

    source venv/bin/activate

Once activated, your terminal prompt will typically change to show the active environment, like this:

.. code-block:: console

    (venv) user@machine:~/project$

Deactivating the Virtual Environment
------------------------------------

To stop using the virtual environment, simply run:

.. code-block:: console

    deactivate

This will return you to your system's default Python environment.

Verifying the Virtual Environment
---------------------------------

You can verify that the virtual environment is active and using the correct Python interpreter by running:

.. code-block:: console

    which python  # Unix/MacOS
    where python  # Windows

You should see a path pointing to the **`venv`** directory.

Installing Packages in the Virtual Environment
----------------------------------------------

With the virtual environment activated, you can install packages using **pip**:

.. code-block:: console

    pip install package_name

To install all dependencies listed in a **`requirements.txt`** file:

.. code-block:: console

    pip install -r requirements.txt

Generating requirements.txt
---------------------------

After installing packages, you can freeze the current environment's dependencies into a **`requirements.txt`** file using:

.. code-block:: console

    pip freeze > requirements.txt

This allows others (or yourself) to recreate the exact environment using:

.. code-block:: console

    pip install -r requirements.txt

