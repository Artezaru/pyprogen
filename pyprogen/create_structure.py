import os
import sys
import subprocess
from typing import List
import importlib.resources as pkg_resources
import json
import time

from .user_data_binder import UserDataBinder

def create_structure(user_data: UserDataBinder) -> None:
    r"""
    Create the project structure according to the user data and the structure.json file.

    .. warning::

        If user_data.git is True, the user must have ``git`` installed on their machine.
        To install git, please refer to the official documentation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

    .. warning::

        If user_data.github is True, the user must have a GitHub account and a repository must be created on GitHub.
        The computer must be linked to the GitHub account otherwise the proccess will freeze because the user can't enter the GitHub credentials during the process.

    It is recommended to use the CLI to create the project structure.

    Parameters
    ----------
    user_data : UserDataBinder
        The user data object.

    Raises
    ------
    ValueError
        If the user data does not contain the necessary information (author_name, author_email, package_name).
        If the user data contains github=True and (author_github is None or git=False).
        If the package name is not valid.
        If the package name already exists.
    FileNotFoundError
        If the structure.json file is not found.
    """

    # 0. Check if the user data contains the information needed and if the package name is valid (no spaces or special characters) and available.
    print("[pyprogen] Checking user data ... ")
    if user_data.author_name is None or user_data.author_email is None or user_data.package_name is None:
        raise ValueError("author_name and author_email must be provided")
    
    if user_data.github and (user_data.author_github is None or not user_data.git):
        raise ValueError("author_github must be provided and git must be True if github is True")

    if not user_data.package_name.isidentifier():
        raise ValueError("Invalid package name")

    if os.path.exists(user_data.package_name):
        raise ValueError("Package name already exists")

    if user_data.author_github is None:
        user_data.author_github = "" # Ensure the format string works correctly

    # 1. Get the structure
    print("[pyprogen] Loading structure ... ")
    filepath = pkg_resources.files('pyprogen.ressources') / 'structure.json'
    with open(filepath) as file:
        structure = json.load(file)

    # 2. Create the dictionnary to format the strings in the templates and paths
    print("[pyprogen] Formatting the structure ... ")
    formatting = {}
    formatting["package_year"] = time.strftime("%Y")
    formatting["package_name"] = user_data.package_name
    formatting["author_name"] = user_data.author_name
    formatting["author_email"] = user_data.author_email
    formatting["author_github"] = user_data.author_github

    # 3. Load the key/path for directories and files to format the strings in the templates
    for key, directory in structure["directories"].items():
        # Format the path
        path = directory["path"].format(**formatting)
        formatting[key] = path

    for key, file in structure["files"].items():
        # Format the path
        path = file["path"].format(**formatting)
        formatting[key] = path

    # 4. Create the directories 
    os.makedirs(user_data.package_name, exist_ok=True)
    os.chdir(user_data.package_name)
    print("[pyprogen] Creating directories ... ")
    for key, directory in structure["directories"].items():
        # Check if the directory should be created
        if directory["if_doc"] and not user_data.doc:
            continue
        if directory["if_git"] and not user_data.git:
            continue
        if directory["if_venv"] and not user_data.venv:
            continue
        
        # Create the directory
        os.makedirs(formatting[key], exist_ok=True)
    
    # 5. Create the files
    print("[pyprogen] Creating files ... ")
    for key, file in structure["files"].items():
        # Check if the file should be created
        if file["if_doc"] and not user_data.doc:
            continue
        if file["if_git"] and not user_data.git:
            continue
        if file["if_venv"] and not user_data.venv:
            continue

        # Load the template
        with pkg_resources.open_text("pyprogen.ressources", file["template"]) as file:
            template = file.read()

        # Format the template
        content = template.format(**formatting)

        # Write the file
        with open(formatting[key], "w") as file:
            file.write(content)

    # 6. Setting up git
    if user_data.git:
        print("[pyprogen] Setting up git ... ")
        os.system(f"git config user.name {user_data.author_name}")
        os.system(f"git config user.email {user_data.author_email}")
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "Initial commit"')

    # 7. Create the virtual environment
    pip_path = "pip" # Default pip
    if user_data.venv:
        print("[pyprogen] Creating virtual environment ... ")
        venv_path = formatting["venv_dir"]
        # Create the virtual environment
        subprocess.run([pip_path, "install", "virtualenv"])
        subprocess.run(["virtualenv", venv_path])

        # Activate the virtual environment and install the required packages
        pip_path = os.path.join(venv_path, "bin", "pip")

    # 8. Installing the package for the documentation
    if user_data.doc:
        print("[pyprogen] Installing documentation tools ... ")
        subprocess.run([pip_path, "install", "sphinx"])
        subprocess.run([pip_path, "install", "pydata_sphinx_theme"])

    # 9. Setting the connection to GitHub
    if user_data.github:
        print("[pyprogen] Setting up GitHub ... ")
        os.system(f"git remote add origin {user_data.author_github}")
        os.system("git push origin master")
    
    print("[pyprogen] Done!")


        


    




        