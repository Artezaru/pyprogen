Ressources files
================

This section contains the template files to restore a broken package.
The structure of the complete package is described in the :doc:`usage_doc/project_structure` section.

Il the various files please replace the following placeholders:

- `{author_name}`: The name(s) of the author of the package. (ex: Artezaru)
- `{author_email}`: The email of the author of the package. (ex: artezaru.github@proton.me)
- `{github_repo}`: The GitHub repository of the package. (ex: https://github.com/Artezaru/pyprogen.git)
- `{gitpage_doc}`: The GitHub page of the package. (ex: https://artezaru.github.io/pyprogen/)
- `{package_name}`: The name of the package. (ex: pyprogen)
- `{*_dir}`: The path of the corresponding directory.
- `{*_file}`: The path of the corresponding file. 

Also replace the `{{` and `}}` by `{` and `}` respectively.

__init__.py
-----------

.. literalinclude:: ../../pyprogen/ressources/package_init.txt

__main__.py
-----------

.. literalinclude:: ../../pyprogen/ressources/package_main.txt

__version__.py
--------------

.. literalinclude:: ../../pyprogen/ressources/package_version.txt

Readme.md
---------

.. literalinclude:: ../../pyprogen/ressources/project_readme.txt

setup.py
--------

.. literalinclude:: ../../pyprogen/ressources/package_setup.txt

requirements.txt
----------------

.. literalinclude:: ../../pyprogen/ressources/package_requirements.txt

LICENSE
-------

.. literalinclude:: ../../pyprogen/ressources/Apache_LICENSE.txt

conf.py
-------

.. literalinclude:: ../../pyprogen/ressources/documentation_conf.txt

Makefile
--------

.. literalinclude:: ../../pyprogen/ressources/documentation_makefile.txt

index.rst
---------

.. literalinclude:: ../../pyprogen/ressources/documentation_index.txt

api.rst
-------

.. literalinclude:: ../../pyprogen/ressources/documentation_api.txt

usage.rst
---------

.. literalinclude:: ../../pyprogen/ressources/documentation_usage.txt

.gitignore
-----------

.. literalinclude:: ../../pyprogen/ressources/gitignore.txt

