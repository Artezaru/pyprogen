import curses
import curses.textpad
from typing import Tuple
from .user_data import UserData

def cli(stdscr) -> Tuple[bool, UserData]:
    """
    CLI to edit the User Data.

    Parameters
    ----------
    stdscr : curses.window
        The standard screen.
    
    Returns
    -------
    bool
        True if the user wants to create the package, False otherwise.
    
    user_data : UserData
        The user data object.
    """
    # Initialize the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Initialize the user data and project data
    user_data = UserData()
    user_data.save_data()

    # Define color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Error color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Create color
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Cancel color
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Command color
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Standard text color

    # Helper Variables
    CONTINUE = [True]
    CREATE = [False]

    # Helper functions
    def get_item_color(item: dict) -> curses.color_pair:
        """
        Get the color of the item.
        """
        if "color" in item.keys():
            return curses.color_pair(item["color"])
        if "get_color" in item.keys():
            return curses.color_pair(item["get_color"]())
        raise ValueError("Item dont have 'color' or 'get_color' attribute")
    
    def get_item_message(item: dict) -> str:
        """
        Get the message of the item.
        """
        if "message" in item.keys():
            return item["message"]
        if "get_message" in item.keys():
            return item["get_message"]()
        raise ValueError("Item dont have 'message' or 'get_message' attribute")
    
    def add_name() -> None:
        """
        Add a new author name.
        """
        user_data.add_author("", "")
    
    def remove_name() -> None:
        """
        Remove the last author name.
        """
        user_data.remove_last_author()

    def autofill() -> None:
        """
        Autofill the project name.
        """
        user_data.auto_fill()

    def next_platform_value() -> str:
        """
        Get the next platform value.
        """
        values = ["", "github", "gitlab"]
        current = user_data.dict_data["platform"]
        index = values.index(current)
        return values[(index + 1) % len(values)]
    
    def create_package() -> None:
        """
        Create the package.
        """
        if user_data.ready_to_create()[0]:
            CREATE[0] = True
            CONTINUE[0] = False
        else:
            CREATE[0] = False
            CONTINUE[0] = True

    def cancel_creation() -> None:
        """
        Cancel the package creation.
        """
        CREATE[0] = False
        CONTINUE[0] = False

    def generate_authors_submenus(CLI_MENUS: list) -> None:
        """
        Generate the authors submenus.
        """
        authors = user_data.dict_data["author_names"]
        # Create the command to add and remove authors
        CLI_MENUS[0]["submenus"] = [
            { 
                "name" : "[ADD]",
                "type" : "command",
                "color" : 4,
                "action" : add_name,
                "message" : "Add a new author."
            },
            {
                "name" : "[REMOVE]",
                "type" : "command",
                "color" : 4,
                "action" : remove_name,
                "message" : "Remove the last author."
            }
        ]
        # Add the authors names and emails
        for i in range(len(authors)):
            CLI_MENUS[0]["submenus"].append(
                {
                    "name" : "name",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda i=i: authors[i]["name"],
                    "set_value" : lambda value, i=i : authors[i].update({"name" : value})
                }
            )
            CLI_MENUS[0]["submenus"].append(
                {
                    "name" : "email",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda i=i: authors[i]["email"],
                    "set_value" : lambda value, i=i : authors[i].update({"email" : value})
                }
            )
        return CLI_MENUS
    
    # Define the menus 
    CLI_MENUS = [
        {   
            "name" : "Authors",
            "color" : 5,
            "nb_columns" : 3,
            "columns" : ["Menu", "Metadata", "Value"],
            "type" : "content",
            "pre_execute" : lambda CLI_MENUS : generate_authors_submenus(CLI_MENUS),
            "submenus" : [
                { 
                    "name" : "[ADD]",
                    "type" : "command",
                    "color" : 4,
                    "action" : add_name,
                    "message" : "Add a new author."
                },
                {
                    "name" : "[REMOVE]",
                    "type" : "command",
                    "color" : 4,
                    "action" : remove_name,
                    "message" : "Remove the last author."
                }
            ]
        },

        {
            "name" : "Project",
            "color" : 5,
            "nb_columns" : 3,
            "columns" : ["Menu", "Metadata", "Value"],
            "type" : "content",
            "submenus" : [
                {
                    "name" : "Package Name",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda : user_data.dict_data["package_name"],
                    "set_value" : lambda value : user_data.dict_data.update({"package_name" : value})
                },
                {
                    "name" : "Package Description",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda : user_data.dict_data["package_description"],
                    "set_value" : lambda value : user_data.dict_data.update({"package_description" : value})
                },
                {
                    "name" : "Platform",
                    "type" : "toggle",
                    "color" : 5,
                    "get_value" : lambda : user_data.dict_data["platform"],
                    "set_value" : lambda value : user_data.dict_data.update({"platform" : value}),
                    "next_value" : lambda : next_platform_value()
                },
                {
                    "name" : "Virtual Environment",
                    "type" : "toggle",
                    "color" : 5,
                    "get_value" : lambda : "yes" if user_data.dict_data["venv"] else "no",
                    "set_value" : lambda value : user_data.dict_data.update({"venv" : value == "yes"}),
                    "next_value" : lambda : "yes" if not user_data.dict_data["venv"] else "no"
                },
                {
                    "name" : "[AUTOFILL]",
                    "type" : "command",
                    "color" : 4,
                    "action" : lambda : autofill(),
                    "message" : "Autofill the project URL."
                },
                {
                    "name" : "Package URL",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda : user_data.dict_data["package_url"],
                    "set_value" : lambda value : user_data.dict_data.update({"package_url" : value})
                },
                {
                    "name" : "Documentation URL",
                    "type" : "edit",
                    "color" : 5,
                    "get_value" : lambda : user_data.dict_data["package_doc"],
                    "set_value" : lambda value : user_data.dict_data.update({"package_doc" : value})
                },
                {
                    "name" : "Remote",
                    "type" : "toggle",
                    "color" : 5,
                    "get_value" : lambda : "yes" if user_data.dict_data["remote"] else "no",
                    "set_value" : lambda value : user_data.dict_data.update({"remote" : value == "yes"}),
                    "next_value" : lambda : "yes" if not user_data.dict_data["remote"] else "no"
                }
            ]
        },

        {
            "name" : "[Create]",
            "get_color" : lambda : 2 if user_data.ready_to_create()[0] else 1,
            "nb_columns" : 2,
            "columns" : ["Menu", "Information"],
            "type" : "command",
            "action" : lambda : create_package(),
            "get_message" : lambda : user_data.ready_to_create()[1] if not user_data.ready_to_create()[0] else "Create the package."
        },

        {
            "name" : "[Cancel]",
            "color" : 3,
            "nb_columns" : 2,
            "columns" : ["Menu", "Information"],
            "type" : "command",
            "action" : lambda : cancel_creation(),
            "message" : "Cancel the package creation."
        }
    ]









    # =================================================================================================
    # Main loop
    # =================================================================================================

    # Cursor position
    current_menu_index = 0
    current_submenu_index = 0
    level = 0

    while CONTINUE[0]:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Pre-execute the menus
        functions = [menu["pre_execute"] for menu in CLI_MENUS if "pre_execute" in menu.keys()]
        for pre_execute in functions:
            CLI_MENUS = pre_execute(CLI_MENUS)

        # Get the current menu and submenu
        current_menu = CLI_MENUS[current_menu_index]

        # Display the columns
        nb_columns = current_menu["nb_columns"]
        column_width = width // nb_columns
        columns = current_menu["columns"]
        for i, column in enumerate(columns):
            stdscr.addstr(0, i * column_width, column, curses.color_pair(5))

        # Starting row to 2 -> jump one row
        start_row = 2

        # Display the menues
        for i, menu in enumerate(CLI_MENUS):
            color = get_item_color(menu)
            name = menu["name"]
            if level == 0 and i == current_menu_index:
                stdscr.addstr(start_row + i, 0, name, color | curses.A_REVERSE)
            else:
                stdscr.addstr(start_row + i, 0, name, color)

        # If the current menu is a content menu, display the submenus
        if current_menu["type"] == "content":
            current_submenu = current_menu["submenus"][current_submenu_index]
            row = start_row
            for i, submenu in enumerate(current_menu["submenus"]):
                color = get_item_color(submenu)
                name = submenu["name"]

                # Case of a command
                if submenu["type"] == "command":
                    message = get_item_message(submenu)
                    if level == 1 and i == current_submenu_index:
                        stdscr.addstr(row, 1*column_width, name, color | curses.A_REVERSE)
                    else:
                        stdscr.addstr(row, 1*column_width, name, color)
                    stdscr.addstr(row, 2*column_width, message, color)
                    row += 1
                
                # Case of a edit
                elif submenu["type"] == "edit":
                    value = submenu["get_value"]()
                    if level == 1 and i == current_submenu_index:
                        stdscr.addstr(row, 1*column_width, name, color | curses.A_REVERSE)
                    else:
                        stdscr.addstr(row, 1*column_width, name, color)
                    stdscr.addstr(row, 2*column_width, value, color)
                    row += 1

                # Case of a toggle
                elif submenu["type"] == "toggle":
                    value = submenu["get_value"]()
                    if level == 1 and i == current_submenu_index:
                        stdscr.addstr(row, 1*column_width, name, color | curses.A_REVERSE)
                    else:
                        stdscr.addstr(row, 1*column_width, name, color)
                    stdscr.addstr(row, 2*column_width, value, color)
                    row += 1

        # if the current menu is a command menu, display the message
        elif current_menu["type"] == "command":
            color = get_item_color(current_menu)
            message = get_item_message(current_menu)
            stdscr.addstr(start_row + current_menu_index, 1*column_width, message, color)

        # Refresh the screen
        stdscr.refresh()

        # Get the user input
        key = stdscr.getch()

        # Process the user input
        if key == curses.KEY_UP:
            if level == 0:
                current_menu_index = (current_menu_index - 1) % len(CLI_MENUS)
            elif level == 1:
                current_submenu_index = (current_submenu_index - 1) % len(current_menu["submenus"])

        elif key == curses.KEY_DOWN:
            if level == 0:
                current_menu_index = (current_menu_index + 1) % len(CLI_MENUS)
            elif level == 1:
                current_submenu_index = (current_submenu_index + 1) % len(current_menu["submenus"])
            
        elif key == curses.KEY_LEFT:
            if level == 1:
                level = 0
                current_submenu_index = 0
        
        elif key == curses.KEY_RIGHT:
            if level == 0:
                # Case of a content menu
                if current_menu["type"] == "content":
                    level = 1
                    current_submenu_index = 0
        
        elif key in [curses.KEY_ENTER, 10, 13, ord("\n")]:
            # Case of a command
            if current_menu["type"] == "command":
                current_menu["action"]()

            # Case of a content
            if level == 1:
                # Case of a edit
                if current_submenu["type"] == "edit":
                    stdscr.addstr(height - 2, 0, "Enter value: ")  # Display prompt at the bottom
                    stdscr.refresh()

                    # Create a small window for input
                    edit_win = curses.newwin(1, width - 15, height - 2, 12)
                    box = curses.textpad.Textbox(edit_win)

                    # Capture user input
                    curses.curs_set(1)  # Show the cursor
                    box.edit()
                    curses.curs_set(0)  # Hide the cursor again
                    
                    # Get input and store it
                    input_value = box.gather().strip()
                    current_submenu["set_value"](input_value)

                # Case of a toggle
                elif current_submenu["type"] == "toggle":
                    current_submenu["set_value"](current_submenu["next_value"]())

                # Case of a command
                elif current_submenu["type"] == "command":
                    current_submenu["action"]()

        elif key == curses.KEY_EXIT:
            break

    return CREATE[0], user_data
