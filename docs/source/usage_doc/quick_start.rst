Quick Start
===========

Prerequisites
-------------

Before using **pyprogen**, ensure that the following dependencies are installed on your system:

- Python 3.6 or higher
- pip
- git (required for Git-related features)

To automatically link a project to a GitHub repository, you must have a **GitHub account** and an existing repository on GitHub.

.. note::

   The following sections provide step-by-step instructions for manually setting up documentation, Git, or a GitHub repository:

   - :doc:`documentation_setup`
   - :doc:`git_setup`
   - :doc:`github_setup`

Installation
------------

To install **pyprogen**, use the following command:

.. code-block:: console

   pip install git+https://github.com/Artezaru/pyprogen.git

Once installed, you can create a new Python project in the current directory using the command line interface (CLI):

.. code-block:: console

   pyprogen

This command launches an interactive CLI where you can configure your project. Use the **arrow keys** to navigate and **Enter** to select options.

CLI Interface Overview
----------------------

Author Information
~~~~~~~~~~~~~~~~~~

.. image:: images/author_informations.png
   :alt: Author Information Section
   :align: center

In this section, you must enter the **author's name** and **email address**. These fields are mandatory.

To modify a field, navigate to it using the arrow keys and press **Enter** to input a new value.

.. note::

   The author information is saved for future use, so you only need to enter it once unless you wish to update it.

Package Setup
~~~~~~~~~~~~~

.. image:: images/package_setup.png
   :alt: Package Setup Section
   :align: center

Here, you configure the project settings, including:

- **Package name** (mandatory)
- Enable **Sphinx documentation** (optional)
- Initialize a **Git repository** (optional)
- Create a **virtual environment** (optional)

.. note::

   Documentation, Git, and virtual environment preferences are saved for future use. Only the **package name** needs to be entered each time you create a new project.

.. warning::

   If Git is enabled, ``git`` must be installed on your system.

GitHub Integration
~~~~~~~~~~~~~~~~~~

.. image:: images/github.png
   :alt: GitHub Section
   :align: center

In this section, you can enter a **GitHub repository URL** to link your project.

.. warning::

   - The repository must already exist on GitHub before creating the project.
   - Your computer must have **access** to the repository, and your **credentials** must be stored in the Git configuration.

Creating the Project
--------------------

Once all fields are filled, click the **"Create"** button to generate the project in the current directory.  
The project structure is detailed in the :doc:`project_structure` section.

.. note::

   If the button appears in **red**, it indicates missing required fields, preventing the project from being created.

To cancel the setup at any time, press the **Exit** button.
