Setting Up GitHub Manually
==========================

If the GitHub repository is not set up automatically, you can configure it manually by following these steps.

Creating a New GitHub Repository
--------------------------------

1. Go to **[GitHub](https://github.com)** and create a **new empty repository**.  
2. **Do not** initialize it with a README, `.gitignore`, or license — these will be added from your local project.

Configuring Git User Information
--------------------------------

In your terminal, navigate to the **root** of your project and configure your Git username and email:

.. code-block:: console

    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

> **Tip:** If you want this configuration to be **project-specific** (instead of global), remove the `--global` flag.

Adding the Remote GitHub Repository
-----------------------------------

Add your GitHub repository as the **remote origin**:

.. code-block:: console

    git remote add origin https://github.com/{username}/{repository_name}.git

- Replace ``{username}`` with your **GitHub username**.  
- Replace ``{repository_name}`` with the **name of your repository**.

You can verify that the remote has been added correctly with:

.. code-block:: console

    git remote -v

Pushing Your Code to GitHub
---------------------------

Once the remote is set up, you can push your code to GitHub. Follow the instructions in the :doc:`use_git` section to properly commit and push your changes.

For a quick initial push, use the following commands:

.. code-block:: console

    git add -A .
    git commit -m "Initial commit"
    git push -u origin master

.. note::

   If you're using **main** as the default branch instead of **master**, replace `master` with `main` in the commands above.

Next Steps
----------

- To set up **GitHub Pages** for hosting documentation, refer to the :doc:`git_setup` section.  
- For pushing documentation to GitHub, refer to the :doc:`use_git` section.
