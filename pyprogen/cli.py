import curses
from typing import Tuple
from .user_data_binder import UserDataBinder
from .create_structure import create_structure
import os


def cli(stdscr):
    r"""
    Run the CLI interface.
    Allows users to navigate through menu options, edit user data, toggle boolean fields, and execute create actions.

    Parameters
    ----------
    stdscr : curses.window
        The curses window object.
    """
    # Initialize the user data
    user_data = UserDataBinder()

    # Set default values
    user_data.package_name = None
    user_data.github_username = None
    user_data.github_email = None
    user_data.github_repo = None
    user_data.gitpage_doc = None
    user_data.github = False

    # Initialize curses settings
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Define the color pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Define the CLI interface
    CLI_INTERFACE = {
        "Author Informations": [
            {"label": "Author Name(s)", "key": "author_name", "type": "text", "required": True},
            {"label": "Author Email", "key": "author_email", "type": "text", "required": True}
        ],
        "Package Setup": [
            {"label": "Package Name", "key": "package_name", "type": "text", "required": True},
            {"label": "Documentation", "key": "doc", "type": "bool", "required": False},
            {"label": "Git", "key": "git", "type": "bool", "required": False},
            {"label": "Virtual Environment", "key": "venv", "type": "bool", "required": False}
        ],
        "GitHub": [
            {"label": "GitHub Enabled", "key": "github", "type": "bool", "required": False},
            {"label": "Auto-Generate", "key": None, "type": "command", "required": False, "condition": "github"},
            {"label": "GitHub Username", "key": "github_username", "type": "text", "required": False, "condition": "github"},
            {"label": "GitHub Email", "key": "github_email", "type": "text", "required": False, "condition": "github"},
            {"label": "GitHub Repository", "key": "github_repo", "type": "text", "required": False, "condition": "github"},
            {"label": "GitHub Pages Documentation", "key": "gitpage_doc", "type": "text", "required": False, "condition": "github"},
        ],
        "Create": [],
        "Cancel": []
    }

    current_option = "Author Informations"
    detail_index = 0
    focus_column = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Calculate column widths
        column_0_width = width // 3
        column_1_width = width - column_0_width - 2

        # Draw columns with focus indicators
        column_0_border = curses.A_BOLD | (curses.A_REVERSE if focus_column == 0 else 0)
        column_1_border = curses.A_BOLD | (curses.A_REVERSE if focus_column == 1 else 0)

        # Draw menu options
        stdscr.addstr(0, 0, "Menu:", column_0_border)
        for idx, option in enumerate(CLI_INTERFACE.keys()):
            if option == "Create":
                valid = user_data.ready_to_create()[0]
                color = curses.color_pair(1) if not valid else curses.color_pair(2)
                highlight = curses.A_REVERSE if focus_column == 0 and option == current_option else curses.A_NORMAL
                stdscr.addstr(idx + 1, 0, f"  {option}", color | highlight)
            else:
                highlight = curses.A_REVERSE if focus_column == 0 and option == current_option else curses.A_NORMAL
                stdscr.addstr(idx + 1, 0, f"  {option}", highlight)

        stdscr.addstr(0, column_0_width + 2, "Details:", column_1_border)

        # Get the current selected section and fields
        selected_section = CLI_INTERFACE[current_option]

        # Display details based on selection
        for idx, field in enumerate(selected_section):
            if "condition" in field and not getattr(user_data, field["condition"], False):
                continue

            if field["key"] is None:
                highlight = curses.A_REVERSE if focus_column == 1 and idx == detail_index else curses.A_NORMAL
                stdscr.addstr(idx + 1, column_0_width + 2, f"{field['label']}", highlight)
                continue

            value = getattr(user_data, field["key"], None)
            display_value = "" if value is None else ("Yes" if isinstance(value, bool) and value else "No" if isinstance(value, bool) else value)

            highlight = curses.A_REVERSE if focus_column == 1 and idx == detail_index else curses.A_NORMAL
            stdscr.addstr(idx + 1, column_0_width + 2, f"{field['label']}: {display_value}", highlight)

        # Additionnal informations
        if current_option == "Package Setup":
            color = curses.color_pair(3)
            stdscr.addstr(len(selected_section) + 2, column_0_width + 2, "If git = Yes, git must be installed on the machine.", color)
        if current_option == "GitHub":
            color = curses.color_pair(3)
            stdscr.addstr(len(selected_section) + 2, column_0_width + 2, "If github = Yes, a repository must be created on GitHub.", color)
            stdscr.addstr(len(selected_section) + 3, column_0_width + 2, "The computer must be linked to the GitHub account.", color)

        # Handle 'Create' option with missing fields
        if current_option == "Create":
            valid, message = user_data.ready_to_create()
            if not valid:
                color = curses.color_pair(1)
                stdscr.addstr(1, column_0_width + 2, message, color)
            else:
                color = curses.color_pair(2)
                stdscr.addstr(1, column_0_width + 2, "Ready to create the package!", color)

        stdscr.refresh()

        # Handle keyboard inputs
        key = stdscr.getch()

        if key == curses.KEY_UP:
            if focus_column == 0:
                option_keys = list(CLI_INTERFACE.keys())
                current_index = option_keys.index(current_option)
                current_option = option_keys[(current_index - 1) % len(option_keys)]
                detail_index = 0
            elif focus_column == 1 and selected_section:
                detail_index = (detail_index - 1) % len(selected_section)

        elif key == curses.KEY_DOWN:
            if focus_column == 0:
                option_keys = list(CLI_INTERFACE.keys())
                current_index = option_keys.index(current_option)
                current_option = option_keys[(current_index + 1) % len(option_keys)]
                detail_index = 0
            elif focus_column == 1 and selected_section:
                detail_index = (detail_index + 1) % len(selected_section)

        elif key == curses.KEY_RIGHT:
            if selected_section:
                focus_column = 1

        elif key == curses.KEY_LEFT:
            focus_column = 0

        elif key == ord('\n'):  # Enter
            if current_option == "Cancel":
                break

            if current_option == "Create":
                valid, error_message = user_data.ready_to_create()
                if not valid:
                    stdscr.addstr(height - 2, 0, error_message)
                    stdscr.getch()
                else:
                    user_data.dump_user_data()
                    stdscr.addstr(height - 2, 0, "Package in progress...")
                    create_structure(user_data)
                    break

            elif focus_column == 1 and selected_section:
                field = selected_section[detail_index]
                if field["type"] == "bool":
                    current_value = getattr(user_data, field["key"], False)
                    setattr(user_data, field["key"], not current_value)

                elif field["type"] == "text":
                    current_value = getattr(user_data, field["key"], "")
                    stdscr.addstr(height - 2, 0, f"Edit {field['label']}: ")
                    curses.echo()
                    new_value = stdscr.getstr(height - 2, len(f"Edit {field['label']}: ")).decode("utf-8").strip()
                    curses.noecho()
                    setattr(user_data, field["key"], new_value if new_value else None)

                elif field["type"] == "command":
                    if current_option == "GitHub" and field["label"] == "Auto-Generate":
                        if user_data.author_name and user_data.package_name:
                            generate_author = user_data.author_name.replace(" ", "-").lower()
                            generate_email = user_data.author_email
                            generated_url = f"https://github.com/{generate_author}/{user_data.package_name}.git"
                            generated_doc = f"https://{generate_author}.github.io/{user_data.package_name}"
                            setattr(user_data, "github_username", generate_author)
                            setattr(user_data, "github_email", generate_email)
                            setattr(user_data, "github_repo", generated_url)
                            setattr(user_data, "gitpage_doc", generated_doc)
                        

if __name__ == '__main__':
    curses.wrapper(cli)
