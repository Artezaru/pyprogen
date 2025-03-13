import os
from typing import List, Tuple
import json
import re
import time

class UserData(object):
    r"""
    Class to store user data.

    The user data is stored in a user.json file under the .pyprogen/ directory in the user's home directory.

    The file has the following content:

    .. code-block:: json

        {
            "author_names": [
                {"name" : "John Doe", "email" : "john.doe@example.com"}
            ],
            "venv": true,
            "platform": "github",
            "remote": true,
        }

    Once the data are get, the data are stored in a dictionnary with the following content:

    .. code-block:: python

        user_data.dict_data = {
            "author_names": [
                {name = "John Doe", email = "john.doe@example.com"}
            ],
            "package_name": "mypackage"
            "package_description": "My package description",
            "venv": True,
            "platform": "github",
            "package_url": "https://github.com/JohnDoe/mypackage.git
            "package_doc": "https://JohnDoe.github.io/mypackage
            "remote": True,
            ...
        }
    """
    __keys__: List[str] = ["author_names", "venv", "package_name", "package_url", "package_doc", "platform", "remote", "author_toml_str", "author_doc_str", "package_description", "first_author", "first_email", "package_year"]
    __load_keys__: List[str] = ["author_names", "venv", "platform", "remote"]
    __str_keys__: List[str] = ["package_name", "package_url", "package_doc", "platform", "author_toml_str", "author_doc_str", "package_description"]
    __bool_keys__: List[str] = ["venv", "remote"]
    __special_keys__: List[str] = ["author_names", "author_toml_str", "author_doc_str", "first_author", "first_email", "package_year"]

    def __init__(self):
        self.directory = os.path.expanduser("~/.pyprogen/")
        self.filepath = os.path.join(self.directory, "user.json")
        os.makedirs(self.directory, exist_ok=True)
        self.load_data()


    def __getitem__(self, key: str):
        if key not in self.__keys__:
            raise KeyError(f"Key {key} not found.")
        return self.dict_data[key]

    def __setitem__(self, key: str, value):
        if key not in self.__keys__:
            raise KeyError(f"Key {key} not found.")
        if key in self.__str_keys__:
            if not isinstance(value, str):
                raise ValueError("The value must be a string.")
        elif key in self.__bool_keys__:
            if not isinstance(value, bool):
                raise ValueError("The value must be a boolean.")
        elif key in self.__special_keys__:
            raise ValueError(f"Use the appropriate method to set the {key} value.")
        self.dict_data[key] = value


    def initialise(self):
        """
        Clear the dictionary data.
        """
        self.dict_data = {
            "author_names": [],
            "venv": True,
            "platform": "",
            "remote": True,
            "package_name": "",
            "package_description": "",
            "package_url": "",
            "package_doc": "",
            "author_toml_str": "",
            "first_author": "",
            "first_email": "",
            "author_doc_str": "",
            "package_year": ""
        }


    def load_data(self):
        """
        Load the user data from the .json file.
        """
        self.initialise()
         
        # Load the data from the file
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                loaded_data = json.load(file)
            
            # Get the data from the file
            for key in self.__load_keys__:
                self.dict_data[key] = loaded_data.get(key, self.dict_data[key])


    def save_data(self):
        """
        Save the user data to the user.json file.
        """
        sub_dict_data = {}
        for key in self.__load_keys__:
            sub_dict_data[key] = self.dict_data[key]
        
        # Create the file
        with open(self.filepath, "w") as file:
            json.dump(sub_dict_data, file, indent=4)

    
    def clear_data(self):
        """
        Clear the user data from the .json file.
        """
        self.initialise()
        self.save_data()

    
    def add_author(self, name: str, email: str):
        """
        Add an author to the list of authors.

        Parameters
        ----------
        name : str
            The name of the author.
        
        email : str
            The email of the author.
        """
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        if not isinstance(email, str):
            raise ValueError("The email must be a string.")
        self.dict_data["author_names"].append({"name": name, "email": email})

    
    def remove_last_author(self):
        """
        Remove the last author from the list of authors.
        """
        if len(self.dict_data["author_names"]) > 0:
            self.dict_data["author_names"].pop()

    
    def remove_empty_authors(self):
        """
        Remove authors with empty names from the list of authors.
        """
        self.dict_data["author_names"] = [author for author in self.dict_data["author_names"] if len(author["name"]) > 0]

    
    def auto_fill(self):
        """
        Auto fill the user data from the first author and the given package name and platform.
        """
        name = self.dict_data["author_names"][0]["name"] if len(self.dict_data["author_names"]) > 0 else ""
        self.dict_data["package_url"] = f"https://{self.dict_data['platform']}.com/{name}/{self.dict_data['package_name']}.git"
        self.dict_data["package_doc"] = f"https://{name}.{self.dict_data['platform']}.io/{self.dict_data['package_name']}"

    
    def prepare_to_create(self):
        """
        Prepare the user data to create a package.
        """
        self.remove_empty_authors()
        self.save_data()
        self.dict_data["author_toml_str"] = "[\n" + ",\n".join([f'{{name = "{author["name"]}", email = "{author["email"]}"}}' for author in self.dict_data["author_names"]]) + "\n]"
        self.dict_data["author_doc_str"] = "\n".join([f"- {author['name']} <{author['email']}>" for author in self.dict_data["author_names"]])
        self.dict_data["first_author"] = self.dict_data["author_names"][0]["name"] if len(self.dict_data["author_names"]) > 0 else ""
        self.dict_data["first_email"] = self.dict_data["author_names"][0]["email"] if len(self.dict_data["author_names"]) > 0 else ""
        self.dict_data["package_year"] = time.strftime("%Y")


    def get_projects(self, path: str = os.getcwd()) -> List[str]:
        """
        Get the list of projects (directories) in the specified directory.
        The name of the projects is the name of the directories.
        """
        return [dirname for dirname in os.listdir(path) if os.path.isdir(os.path.join(path, dirname))]
    

    def exist_project(self, project_name: str, path: str = os.getcwd()) -> bool:
        """
        Check if the project exists in the specified directory.
        """
        return project_name in self.get_projects(path)


    def check_project_name(self, project_name: str) -> bool:
        """
        Check if the project name is valid.
        The name must be a valid Python identifier or follow a different regex pattern.
        """
        # Validating with a basic regex for a more flexible name check
        return bool(re.match(r'^[a-zA-Z0-9-_]+$', project_name))
    

    def ready_to_create(self) -> Tuple[bool, str]:
        """
        Check if the user data contains the necessary information to create a package.
        """
        if len(self.dict_data["author_names"]) == 0:
            return False, "No author are provided."
        if all([len(author["name"]) == 0 for author in self.dict_data["author_names"]]):
            return False, "All authors have empty names."
        if len(self.dict_data["package_name"]) == 0:
            return False, "No package name is provided."
        if not self.check_project_name(self.dict_data["package_name"]):
            return False, "The package name is not valid."
        if self.exist_project(self.dict_data["package_name"]):
            return False, "The project already exists."
        return True, ""

