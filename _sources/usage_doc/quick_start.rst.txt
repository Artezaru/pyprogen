Quick Start
===========

To use pyprogen, install the package using pip:

.. code-block:: console

    pip install git+https://github.com/Artezaru/pyprogen.git

Then, you can use (in the same environment) the command line interface (CLI) to create a new Python project in the current directory.

.. code-block:: console

    pyprogen

This command will open the following CLI.
You can navigate through the different options with the arrow keys and select an option with the enter key.

The first section is ``Author Informations``.

.. image:: images/author_informations.png
   :alt: Author Informations Section
   :align: center

In this section, you can enter the author name and email. 
These fields are mandatory.
To change the value of a field, you can use the arrow keys to navigate to the field and press the enter key.
Then, a prompt will appear to enter the new value.
The ``Author Informations`` section is saved for the next time you use the CLI. 
It is not necessary to enter this information every time you create a new project but only when you want to change it.

The second section is ``Package Setup``.

.. image:: images/package_setup.png
   :alt: Package Setup Section
   :align: center

In this section, you can enter the package name, and if you want to add a sphinx documentation, a git repository, and create a virtual environment.
The package name is mandatory, but the other fields are optional.
The documention, git and virtual environment fields are saved for the next time you use the CLI.
Only the package name is mandatory to enter every time you create a new project.

.. warning::

        If git is selected, ``git`` must be installed on the system.

The last section is ``GitHub``.

.. image:: images/github.png
   :alt: Github Section
   :align: center

In this section, you can enter the github repository link to connect the project to the repository.

.. warning::

    If github is selected, the git repository must be created on github before creating the project.
    Furthermore, the computer must have access to the repository and the credantials must be saved in the git configuration.
    If the condition is not met, set github to ``No`` and run the following command in the project directory to connect the project to the repository:

    .. code-block:: console

        git remote add origin <repository_link>
        git push -u origin master

After entering all the information, the project will be created in the current directory with the ``Create`` button.

.. note::

    If the button is in red, it means that the project will not be created because some fields are missing.

If you want to cancel the creation, you can press the ``Exit`` keyboard key.