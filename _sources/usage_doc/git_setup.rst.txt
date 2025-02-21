Setting Up Git Manually
=======================

If the Git repository is not set up automatically, you can configure it manually by following these steps.

Installing Git
--------------

First, ensure that **Git** is installed on your system. If it is not installed, follow the official guide:  
`Git Installation Guide <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_

Initializing the Git Repository
-------------------------------

Navigate to the **root** of your project and initialize a new Git repository:

.. code-block:: console

    git init

Next, add a ``.gitignore`` file to the root directory to specify files and folders that Git should ignore.  
You can find a template for this file in the :doc:`../ressources` section.

Add all project files to the repository:

.. code-block:: console

    git add -A .

Then, make your initial commit:

.. code-block:: console

    git commit -m "Initial commit"

Hosting Documentation on GitHub Pages
-------------------------------------

To host your documentation on **GitHub Pages**, you need to create a dedicated branch called ``gh-pages``. Follow these steps:

1. **Navigate** to the `docs/build/html` directory:

   .. code-block:: console

       cd docs/build/html

2. **Create an orphan branch** (a branch with no commit history) for GitHub Pages:

   .. code-block:: console

       git checkout --orphan gh-pages

3. **Reset** the branch to remove any existing files:

   .. code-block:: console

       git reset --hard

4. **Make an initial empty commit** on the `gh-pages` branch:

   .. code-block:: console

       git commit --allow-empty -m "Initial commit"

5. **Return** to the parent directory (`docs/build`) and switch back to the `master` branch:

   .. code-block:: console

       git checkout master

6. **Remove** the existing `html` folder to prepare for linking the `gh-pages` branch:

   .. code-block:: console

       rm -rf html

7. **Link** the `gh-pages` branch to the `html` folder using Git worktree:

   .. code-block:: console

       git worktree add -f html gh-pages

Project Branches Overview
-------------------------

- The **master** branch will serve as the main branch for your project's code.
- The **gh-pages** branch will host the generated documentation on **GitHub Pages**.

.. note::

   To connect the local Git repository to a remote **GitHub** repository, follow the steps in the :doc:`github_setup` section.

.. note::

   For more information on using Git in your project and pushing updates to the `gh-pages` branch, see the :doc:`use_git` section.
