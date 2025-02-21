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
    def author_github(self) -> Optional[str]:
        """
        Getter and setter for the author_github property.

        Parameters
        ----------
        value : Optional[str]
            The value to set the author_github property to.
        
        Raises
        ------
        TypeError
            If the value is not a string and is not None.
        """
        return self.user_data['author_github']
    
    @author_github.setter
    def author_github(self, value: Optional[str]) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("author_github must be a string")
        self.user_data['author_github'] = value

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

        The user_data.json file contains the following structure:

        .. code-block:: json

            {
                "author_name": null,
                "author_email": null,
                "author_github": null,
                "package_name": null,
                "doc": true,
                "git": true,
                "github": false,
                "venv": true
            }

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

    

    