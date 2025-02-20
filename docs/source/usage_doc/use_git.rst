Using Git
=========

Once you have created a new project by the CLI, (see :doc:`quick_start` section). 
You can start using Git to version your project.

.. seealso::

    Also, to learn how to use Git, refer to the `Git Documentation <https://git-scm.com/doc>`_.
    A short guide is available below for the most common commands.

To save the current state of your project, you can run the following commands in the root of the project:

.. code-block:: console

    git add -A .
    git commit -m "<message>"

When your project is ready to be shared to Github, you can push it to a remote repository by running the following command:

.. code-block:: console

    git push origin master

I recommend creating a new branch for each new feature or bug fix.
You can also set the version of the project in the ``__version__.py`` file.
This new version will be saved in the ``setup.py`` file and in the documentation.

.. code-block:: python

    __version__ = "1.0.2"

