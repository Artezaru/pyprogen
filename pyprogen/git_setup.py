import os
from .user_data import UserData

def git_setup(user_data: UserData, check: bool = True):
    r"""
    Initialize the git repository.
    
    Parameters
    ----------
    user_data : UserData
        The user data object.

    Raises
    ------
    ValueError
        If the UserData object is not ready to be used.
        If the package is not created.
    """
    # Check if the user data is ready to be used.
    if not user_data.ready_to_create()[0] and check:
        raise ValueError("The user data is not ready to be used.")
    user_data.prepare_to_create()
    
    # Check if the package is already created.
    current_directory = os.getcwd()
    if not os.path.exists(os.path.join(current_directory, user_data["package_name"])):
        raise ValueError("The package is not created.")

    # Initialize the git repository.
    print("[pyprogen] Initializing the git repository ... ")
    os.chdir(os.path.join(current_directory, user_data["package_name"]))
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

    # Add the gh-pages branch.
    os.system("git checkout --orphan gh-pages")
    os.system("git reset --hard")
    os.system("git commit --allow-empty -m 'Initial commit'")
    os.system("git checkout master")

    # Add the remote repository.
    if user_data["remote"]:
        os.system(f"git remote add origin {user_data['package_url']}")
        os.system("git push -u origin master")
        os.system("git checkout gh-pages")
        os.system("git push -u origin gh-pages")
        os.system("git checkout master")

    os.chdir(current_directory)
    print("[pyprogen] Git repository initialized.")
    


    