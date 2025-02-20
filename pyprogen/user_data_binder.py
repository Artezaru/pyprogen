import json
from typing import Optional
import importlib.resources as pkg_resources

class UserDataBinder:
    r"""
    Class to store user data.

    The user data is stored in the user_data.json file in the pyprogen.ressources package.

    Properties
    ----------
    author_name : Optional[str]
        The name of the author of the project.
    
    author_email : Optional[str]
        The email of the author of the project.

    author_github : Optional[str]
        The GitHub project page of the author of the project.

    package_name : Optional[str]
        The name of the package to create
    
    doc : bool
        Whether to create a documentation folder.
    
    git : bool
        Whether to create a git repository.

    github : bool
        Whether to create a GitHub repository.
    
    venv : bool
        Whether to create a virtual environment.

    """

    def __init__(self) -> None:
        self.load_user_data()

    @property
    def author_name(self) -> Optional[str]:
        return self.user_data['author_name']
    
    @author_name.setter
    def author_name(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_name must be a string")
        self.user_data['author_name'] = value

    @property
    def author_email(self) -> Optional[str]:
        return self.user_data['author_email']
    
    @author_email.setter
    def author_email(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_email must be a string")
        self.user_data['author_email'] = value
    
    @property
    def author_github(self) -> Optional[str]:
        return self.user_data['author_github']
    
    @author_github.setter
    def author_github(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_github must be a string")
        self.user_data['author_github'] = value

    @property
    def package_name(self) -> Optional[str]:
        return self.user_data['package_name']
    
    @package_name.setter
    def package_name(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("package_name must be a string")
        self.user_data['package_name'] = value
    
    @property
    def doc(self) -> bool:
        return self.user_data['doc']
    
    @doc.setter
    def doc(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("doc must be a boolean")
        self.user_data['doc'] = value
    
    @property
    def git(self) -> bool:
        return self.user_data['git']
    
    @git.setter
    def git(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("git must be a boolean")
        self.user_data['git'] = value
    
    @property
    def github(self) -> bool:
        return self.user_data['github']
    
    @github.setter
    def github(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("github must be a boolean")
        self.user_data['github'] = value
    
    @property
    def venv(self) -> bool:
        return self.user_data['venv']
    
    @venv.setter
    def venv(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("venv must be a boolean")
        self.user_data['venv'] = value

    def load_user_data(self) -> None:
        """
        Load user data from the user_data.json file.
        """
        filepath = pkg_resources.files('pyprogen.ressources') / 'user_data.json'
        with open(filepath) as file:
            self.user_data = json.load(file)

    def dump_user_data(self) -> None:
        """
        Dump user data to the user_data.json file.
        """
        filepath = pkg_resources.files('pyprogen.ressources') / 'user_data.json'
        with open(filepath, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    

    