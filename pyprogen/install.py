import os
import subprocess
from .user_data import UserData

def install(user_data: UserData, check: bool = True):
    """
    Create a virtual environment and install the required packages.

    Parameters
    ----------
    user_data : UserDataBinder
        The user data object.

    Raises
    ------
    ValueError
        If the UserData object is not ready to be used.
        If the package is not created
    """
    # Check if the user data is ready to be used.
    if not user_data.ready_to_create()[0] and check:
        raise ValueError("The user data is not ready to be used.")
    user_data.prepare_to_create()
    
    # Check if the package is already created.
    current_directory = os.getcwd()
    if not os.path.exists(os.path.join(current_directory, user_data["package_name"])):
        raise ValueError("The package is not created.")
    
    # Create the virtual environment.
    print("[pyprogen] Creating the virtual environment ... ")
    pip_path = "pip" # Default pip
    if user_data["venv"]:
        venv_path = os.path.join(current_directory, user_data["package_name"], "venv")
        subprocess.run(["python", "-m", "venv", venv_path])
        pip_path = os.path.join(current_directory, user_data["package_name"], "venv", "bin", "pip")
    
    # Install the required packages.
    print("[pyprogen] Installing the required packages ... ")
    os.chdir(os.path.join(current_directory, user_data["package_name"]))
    subprocess.run([pip_path, "install", "-e", ".[dev]"])
    os.chdir(current_directory)
    print("[pyprogen] Required packages installed.")


