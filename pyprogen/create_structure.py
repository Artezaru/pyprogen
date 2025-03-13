import os
from typing import Any, Dict
import importlib.resources as pkg_resources

def create_structure(key: str, value: Any, path: str, formatting: Dict[str, str]):
    """"
    Create the structure of the project according the given structure.

    The structure must be a dictionary with the following structure:

    .. code-block:: json

        {
            "project_name": {
                "src": {
                    "package_name": {
                        "module_name.py": "module_template"
                    }
                }
            }
        }

    The keys are the names of the directories and the values are the names of the files.
    The values are the templates of the files to find in the .ressources/ directory.

    Parameters
    ----------
    key : str
        The key of the structure.
    
    value : Any
        The value of the structure.
    
    path : str
        The path of the structure.
    
    formatting : Dict[str, str]
        The dictionary to format the strings in the templates and paths.
    
    Raises
    ------
    ValueError
        If the value is not a string or a dictionary.
    """
    # Check the input values.
    if not isinstance(value, (str, dict)):
        raise ValueError("The value must be a string or a dictionary.")
    if not isinstance(key, str):
        raise ValueError("The key must be a string.")
    
    # Format the key and the value.
    key = key.format(**formatting)

    # If dictionary, go deeper in the structure.
    if isinstance(value, dict):
        # Empty dictionary, create the directory.
        if len(value.keys()) == 0:
            os.makedirs(path, exist_ok=True)
        
        # Go deeper in the structure.
        for subkey, subvalue in value.items():
            create_structure(subkey, subvalue, os.path.join(path, key), formatting)
    
    # If string, create the file.
    if isinstance(value, str):
        # Format the value.
        value = value.format(**formatting)

        # Create the file.
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, key)
        templatepath = pkg_resources.files('pyprogen.ressources') / f"{value}"

        with open(templatepath, "r") as templatefile:
            template = templatefile.read()
    
        template = template.format(**formatting)

        with open(filepath, "w") as file:
            file.write(template)

    return None


        