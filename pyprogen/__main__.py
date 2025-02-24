from .cli import cli
from .create_structure import create_structure
import curses

def main():
    r"""
    Main function to run the CLI application from the command line.
    """
    create, user_data = curses.wrapper(cli)
    if create:
        create_structure(user_data)
    else:
        print("Package creation cancelled.")
    
if __name__ == "__main__":
    main()
