Git Commit and Push
===================

When you add a new function to the package, you must commit the changes to the repository. To do this, follow these steps:

Update the Package Version
---------------------------

Before committing the changes, you must update the package version. 
To do this, run the following command:

.. code-block:: bash

    make bump

This command will update the version in the ``__version__.py`` file with ``bumpver``.
For example (if the current version is 0.1.0), the new version will be 0.1.1.

If the update is a major or minor version, you can specify the version type by running the following command:

.. code-block:: bash

    make bump level=major

.. note::

    - level=major: This command will update the first number of the version to the next major version. For example, if the current version is 1.4.2, the new version will be 2.0.0.
    - level=minor: This command will update the second number of the version to the next minor version. For example, if the current version is 1.4.2, the new version will be 1.5.0.
    - level=patch: This command will update the third number of the version to the next patch version. For example, if the current version is 1.4.2, the new version will be 1.4.3.
    - By default, the level is set to patch.

Commit the Changes
------------------

After updating the version, you must commit the changes to the repository.

Classic Method
~~~~~~~~~~~~~~

To commit the changes, run the following commands:

.. code-block:: bash

    git add .
    git commit -m "Add the subtraction function"

Then, if you want to push the changes to the repository, run the following command:

.. code-block:: bash

    git push origin master

Alternative Method
~~~~~~~~~~~~~~~~~~

If you want to push the changes to the repository directly, you can use the following command:

.. code-block:: bash

    make git message="Add the subtraction function"

This command will add all the changes, commit them with the message "Add the subtraction function", and push them to the repository.

To see the repository changes, go to the repository page on GitHub or GitLab at the following URL:

- GitHub: https://github.com/<username>/<repository_name>
- GitLab: https://gitlab.com/<username>/<repository_name>

Publish the Documentation
-------------------------

When the changes are pushed to the repository, the workflow will automatically publish the documentation to the `GitHub Pages` or `GitLab Pages` of the project.

To access the documentation, go to the following URL:

- GitHub Pages: https://<username>.github.io/<repository_name>
- GitLab Pages: https://<username>.gitlab.io/<repository_name>
