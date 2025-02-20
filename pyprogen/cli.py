import curses
from .user_data_binder import UserDataBinder
from .create_structure import create_structure

def cli(stdscr):
    r"""
    Run the CLI interface.
    Allows users to navigate through menu options, edit user data, toggle boolean fields,
    and execute create actions.
    """
    # Initialize the user data
    user_data = UserDataBinder()
    
    # Set default values
    user_data.package_name = None
    user_data.author_github = None
    user_data.github = False

    # Initialize curses settings
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    CLI_INTERFACE = {
        "Author Information": [
            {"label": "Author Name", "key": "author_name", "type": "text", "required": True},
            {"label": "Author Email", "key": "author_email", "type": "text", "required": True}
        ],
        "Package Information": [
            {"label": "Package Name", "key": "package_name", "type": "text", "required": True},
            {"label": "Documentation", "key": "doc", "type": "bool", "required": False},
            {"label": "Git", "key": "git", "type": "bool", "required": False},
            {"label": "Virtual Environment", "key": "venv", "type": "bool", "required": False}
        ],
        "GitHub Information": [
            {"label": "GitHub Enabled", "key": "github", "type": "bool", "required": False},
            {"label": "Auto-Generate", "key": None, "type": "command", "required": False, "condition": "github"},
            {"label": "Author GitHub", "key": "author_github", "type": "text", "required": False, "condition": "github"}
        ],
        "Create": []
    }

    current_option = "Author Information"
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
            highlight = curses.A_REVERSE if focus_column == 0 and option == current_option else curses.A_NORMAL
            stdscr.addstr(idx + 1, 0, f"  {option}", highlight)

        stdscr.addstr(0, column_0_width + 2, "Details:", column_1_border)

        # Get the current selected section and fields
        selected_section = CLI_INTERFACE[current_option]

        # Display details based on selection
        for idx, field in enumerate(selected_section):
            # Check for conditions (e.g., only show GitHub link if GitHub is enabled)
            if "condition" in field and not getattr(user_data, field["condition"], False):
                continue
            
            # Skip non-editable fields
            if field["key"] is None:
                highlight = curses.A_REVERSE if focus_column == 1 and idx == detail_index else curses.A_NORMAL
                stdscr.addstr(idx + 1, column_0_width + 2, f"{field['label']}", highlight)
                continue 

            value = getattr(user_data, field["key"])
            if value is None:
                display_value = ""
            elif isinstance(value, bool):
                display_value = "Yes" if value else "No"
            else:
                display_value = value

            highlight = curses.A_REVERSE if focus_column == 1 and idx == detail_index else curses.A_NORMAL
            stdscr.addstr(idx + 1, column_0_width + 2, f"{field['label']}: {display_value}", highlight)

        # Highlight 'Create' in red if required fields are missing
        if current_option == "Create":
            missing_fields = [
                field["label"] for section in CLI_INTERFACE.values() for field in section
                if field.get("required") and not getattr(user_data, field["key"], "")
            ]
            if missing_fields:
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
                color = curses.color_pair(1)
                stdscr.addstr(1, column_0_width + 2, "Press Enter to Create (Missing Fields)", color)
            elif user_data.github and not (user_data.author_github and user_data.git):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
                color = curses.color_pair(1)
                stdscr.addstr(1, column_0_width + 2, "Press Enter to Create (GitHub Requires Git and Author GitHub)", color)
            elif not user_data.package_name.isidentifier() or os.path.exists(user_data.package_name):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
                color = curses.color_pair(1)
                stdscr.addstr(1, column_0_width + 2, "Press Enter to Create (Invalid Package Name)", color)
            else:
                stdscr.addstr(1, column_0_width + 2, "Press Enter to Create", curses.A_NORMAL)

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
            if current_option == "Create":
                missing_fields = [
                    field["label"] for section in CLI_INTERFACE.values() for field in section
                    if field.get("required") and not getattr(user_data, field["key"], "")
                ]
                if missing_fields:
                    stdscr.addstr(height - 2, 0, f"Missing required fields: {', '.join(missing_fields)}")
                    stdscr.getch()
                elif user_data.github and not (user_data.author_github and user_data.git):
                    stdscr.addstr(height - 2, 0, "GitHub requires Git and Author GitHub to be set")
                    stdscr.getch()
                elif not user_data.package_name.isidentifier() or os.path.exists(user_data.package_name):
                    stdscr.addstr(height - 2, 0, "Invalid package name")
                    stdscr.getch()
                else:
                    user_data.dump_user_data()
                    stdscr.addstr(height - 2, 0, "Package in progress...")
                    create_structure(user_data)
                    break
            elif focus_column == 1 and selected_section:
                field = selected_section[detail_index]
                if field["type"] == "bool":
                    current_value = getattr(user_data, field["key"], "")
                    setattr(user_data, field["key"], not current_value)
                elif field["type"] == "text":
                    current_value = getattr(user_data, field["key"], "")
                    stdscr.addstr(height - 2, 0, f"Edit {field['label']}: ")
                    curses.echo()
                    new_value = stdscr.getstr(height - 2, len(f"Edit {field['label']}: ")).decode("utf-8").strip()
                    curses.noecho()
                    if len(new_value) == 0:
                        new_value = None
                    setattr(user_data, field["key"], new_value if new_value else current_value)
                elif field["type"] == "command":
                    if current_option == "GitHub Information" and field["label"] == "Auto-Generate":
                        setattr(user_data, "author_github", f"https://github.com/{user_data.author_name}/{user_data.package_name}.git")

        elif key == ord('\x1b'):
            break

if __name__ == '__main__':
    curses.wrapper(cli)