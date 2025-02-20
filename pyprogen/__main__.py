from .cli import cli
import curses

def main():
    r"""
    Main function to run the CLI application from the command line.
    """
    curses.wrapper(cli)
    
if __name__ == "__main__":
    main()
