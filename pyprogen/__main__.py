from .cli import cli
from .run_progen import run_progen
import curses

def __main__() -> None:
    r"""
    Main entry point of the package.

    This method contains the script to run if the user enter the name of the package on the command line. 

    .. code-block:: console
        pyprogen
        
    """
    create, user_data = curses.wrapper(cli)
    if create:
        run_progen(user_data)
    else:
        print("Package creation cancelled.")
    

def __main_gui__() -> None:
    r"""
    Graphical user interface entry point of the package.

    This method contains the script to run if the user enter the name of the package on the command line with the ``gui`` extension.

    .. code-block:: console
        pyprogen-gui
        
    """
    raise NotImplementedError("The graphical user interface entry point is not implemented yet.")

