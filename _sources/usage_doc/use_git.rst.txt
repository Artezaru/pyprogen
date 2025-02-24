Using Git to Commit, Push Code & Build Documentation
====================================================

This guide explains how to **commit**, **push** your **package**, and **build** and **deploy** its **documentation** using **Git** and **GitHub Pages**.

.. seealso::

    For more details on Git commands, refer to the `Git Documentation <https://git-scm.com/doc>`_.

Before you begin, ensure you have updating the version of your package in ``__version__.py`` (see :doc:`project_structure` section).
You must have followed the steps in the :doc:`documentation_setup`, :doc:`git_setup`, and :doc:`github_setup` sections.

Committing and Pushing the Package
----------------------------------

1. **Stage all changes** in the project directory:

   .. code-block:: console

       git add -A .

2. **Commit** the changes with a descriptive message:

   .. code-block:: console

       git commit -m "Add new feature / Fix bug / Update version"

3. **Push** to the remote repository:

   .. code-block:: console

       git push origin master

   > **Note:** Replace `master` with `main` if that's your default branch.

Building and Pushing Documentation
----------------------------------

After updating your code and documentation, follow these steps to **build** and **deploy** the documentation using **Sphinx** and **GitHub Pages**.

1. Build the Documentation
**************************

1. **Activate** the virtual environment:

   .. code-block:: console

       source venv/bin/activate  # On Unix/MacOS
       venv\Scripts\activate.bat  # On Windows

2. **Install** Sphinx and required dependencies (if not already installed):

   .. code-block:: console

       pip install sphinx pydata_sphinx_theme

3. **Clean** any previous build artifacts:

   .. code-block:: console

       make clean

4. **Build** the HTML documentation:

   .. code-block:: console

       make html

   The generated documentation will be located in `docs/build/html/`.

2. Deploy Documentation to GitHub Pages
****************************************

1. **Navigate** to the built documentation:

   .. code-block:: console

       cd docs/build/html

2. **Switch** to the `gh-pages` branch if not already on it:

To check if the `gh-pages` branch is the current branch, run:

.. code-block:: console

    git branch

If not on the `gh-pages` branch, switch to it:

.. code-block:: console

    git checkout gh-pages

3. **Stage** and **commit** the documentation:

   .. code-block:: console

       git add -A .
       git commit -m "Update documentation"

4. **Push** to the `gh-pages` branch:

   .. code-block:: console

       git push origin gh-pages

5. **Return** to the project root:

   .. code-block:: console

       cd ../../..

Best Practices
--------------

- Use **clear commit messages** for both code and documentation.
- Always run **`make clean`** before **`make html`** to avoid stale builds.
- Keep documentation updated with **each new release**.
- **Tag** stable versions for easy tracking.
- Use **separate branches** (e.g., `gh-pages`) for hosting documentation.

Next Steps
----------

- To learn how to **write modules and document them**, see :doc:`write_module_and_doc`.
