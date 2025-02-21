import json
import os 
from typing import Optional, Tuple
import importlib.resources as pkg_resources

class UserDataBinder:
    r"""
    Class to store user data.

    The user data is stored in the user_data.json file in the pyprogen.ressources package.

    The user_data.json file contains the following structure:

        .. code-block:: json

            {
                "author_name": null,
                "author_email": null,
                "github_username": null,
                "github_email": null,
                "github_repo": null,
                "gitpage_doc": null,
                "package_name": null,
                "doc": true,
                "git": true,
                "github": false,
                "venv": true
            }

    Properties
    ----------
    author_name : Optional[str]
        The name of the author of the project.
    
    author_email : Optional[str]
        The email of the author of the project.

    github_username : Optional[str]
        The GitHub username of the author of the project.
    
    github_email : Optional[str]
        The GitHub email of the author of the project.

    github_repo : Optional[str]
        The GitHub project page of the author of the project.

    gitpage_doc : Optional[str]
        The GitHub page of the project.

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
        """
        Getter and setter for the author_name property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the author_name property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['author_name']
    
    @author_name.setter
    def author_name(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_name must be a string")
        self.user_data['author_name'] = value

    @property
    def author_email(self) -> Optional[str]:
        """
        Getter and setter for the author_email property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the author_email property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['author_email']
    
    @author_email.setter
    def author_email(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_email must be a string")
        self.user_data['author_email'] = value

    @property
    def github_username(self) -> Optional[str]:
        """
        Getter and setter for the github_username property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the github_username property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['github_username']
    
    @github_username.setter
    def github_username(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("github_username must be a string")
        self.user_data['github_username'] = value
    
    @property
    def github_email(self) -> Optional[str]:
        """
        Getter and setter for the github_email property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the github_email property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['github_email']
    
    @github_email.setter
    def github_email(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("github_email must be a string")
        self.user_data['github_email'] = value
    
    @property
    def github_repo(self) -> Optional[str]:
        """
        Getter and setter for the github_repo property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the github_repo property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['github_repo']
    
    @github_repo.setter
    def github_repo(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("github_repo must be a string")
        self.user_data['github_repo'] = value

    @property
    def gitpage_doc(self) -> Optional[str]:
        """
        Getter and setter for the gitpage_doc property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the gitpage_doc property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['gitpage_doc']
    
    @gitpage_doc.setter
    def gitpage_doc(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("gitpage_doc must be a string")
        self.user_data['gitpage_doc'] = value

    @property
    def package_name(self) -> Optional[str]:
        """
        Getter and setter for the package_name property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the package_name property to.
        
        Raises
        ------
        TypeError 
            If the value is not a string and is not None.
        """
        return self.user_data['package_name']
    
    @package_name.setter
    def package_name(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("package_name must be a string")
        self.user_data['package_name'] = value
    
    @property
    def doc(self) -> bool:
        """
        Getter and setter for the doc property.

        Parameters
        ----------
        value : bool
            The value to set the doc property to.
        
        Raises
        ------
        TypeError
            If the value is not a boolean.
        """
        return self.user_data['doc']
    
    @doc.setter
    def doc(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("doc must be a boolean")
        self.user_data['doc'] = value
    
    @property
    def git(self) -> bool:
        """
        Getter and setter for the git property.

        Parameters
        ----------
        value : bool
            The value to set the git property to.
        
        Raises
        ------
        TypeError
            If the value is not a boolean.
        """
        return self.user_data['git']
    
    @git.setter
    def git(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("git must be a boolean")
        self.user_data['git'] = value
    
    @property
    def github(self) -> bool:
        """
        Getter and setter for the github property.

        Parameters
        ----------
        value : bool
            The value to set the github property to.
        
        Raises
        ------
        TypeError
            If the value is not a boolean.
        """
        return self.user_data['github']
    
    @github.setter
    def github(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("github must be a boolean")
        self.user_data['github'] = value
    
    @property
    def venv(self) -> bool:
        """
        Getter and setter for the venv property.

        Parameters
        ----------
        value : bool
            The value to set the venv property to.

        Raises
        ------
        TypeError
            If the value is not a boolean.
        """
        return self.user_data['venv']
    
    @venv.setter
    def venv(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("venv must be a boolean")
        self.user_data['venv'] = value

    def load_user_data(self) -> None:
        """
        Load user data from the user_data.json file in the pyprogen.ressources package.

        Raises
        ------
        FileNotFoundError
            If the user_data.json file is not found.
        """
        filepath = pkg_resources.files('pyprogen.ressources') / 'user_data.json'
        with open(filepath) as file:
            self.user_data = json.load(file)

    def dump_user_data(self) -> None:
        """
        Dump user data to the user_data.json file in the pyprogen.ressources package.
        """
        filepath = pkg_resources.files('pyprogen.ressources') / 'user_data.json'
        with open(filepath, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def ready_to_create(self) -> Tuple[bool, str]:
        """
        Check if the user data is ready to create the package.

        The package can be created if the following conditions are met:

        - The author name, author email, and package name are provided.
        - The package name is a valid identifier.
        - The package name does not already exist.
        - If github is True, the github_repo, gitpage_doc, github_author, and github_email are provided and git is True.

        Returns
        -------
        bool
            True if the user data is ready to create the package, False otherwise.
        str
            The error message if the user data is not ready to create the package.
        """
        if self.author_name is None or self.author_email is None or self.package_name is None:
            return False, "The author name, author email, and package name must be provided."
        if self.github and (self.github_username is None or self.github_email is None or self.github_repo is None or self.gitpage_doc is None or not self.git):
            return False, "The GitHub username, GitHub email, GitHub repository, and GitHub pages documentation must be provided."
        if not self.package_name.isidentifier():
            return False, "The package name must be a valid identifier."
        if os.path.exists(self.package_name):
            return False, "The package name already exists."
        return True, ""


    

    