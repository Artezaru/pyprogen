from .user_data import UserData
from .create_structure import create_structure
import importlib.resources as pkg_resources
import json
import os

def construct_project(user_data: UserData, check: bool = True):
    """
    Construct the project structure from the ``.ressources/project_structure.json`` file.

    Parameters
    ----------
    user_data : UserDataBinder
        The user data object.

    Raises
    ------
    ValueError
        If the UserData object is not ready to be used.
    FileNotFoundError
        If the project_structure.json file is not found.
    """
    # Check if the user data is ready to be used.
    if not user_data.ready_to_create()[0] and check:
        raise ValueError("The user data is not ready to be used.")
    user_data.prepare_to_create()

    # Load the project structure from the project_structure.json file.
    print("[pyprogen] Loading structure ... ")
    filepath = pkg_resources.files('pyprogen.ressources') / 'project_structure.json'
    with open(filepath) as file:
        structure = json.load(file)

    # Create the dictionary to format the strings in the templates and paths.
    print("[pyprogen] Formatting the structure ... ")
    formatting = {}
    for key, value in user_data.dict_data.items():
        formatting[key] = value

    # Create the structure of the project.
    print("[pyprogen] Creating the structure ... ")
    current_directory = os.getcwd()
    create_structure("", structure, current_directory, formatting)
            