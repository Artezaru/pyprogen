Create an executable
=====================

If the package has a GUI (see section :doc:`create_command` and ``__main_gui__.py``) and you want to create an executable for it, you can use ``pyinstaller``. 
``pyprogen`` provides a script to create the executable for you.

.. code-block:: bash

    make app

This will create an executable in the ``dist`` directory.

If you want to create an executable for a package without a GUI and run ``__main__.py`` directly, you should open the Makefile and change ``__main_gui__.py`` to ``__main__.py`` in the ``make app`` command.
