from .construct_project import construct_project
from .install import install
from .user_data import UserData
from .git_setup import git_setup

def run_progen(user_data: UserData) -> None:
    r"""
    Run the package creation process.

    Parameters
    ----------
    user_data : UserData
        User data to create the package.
    """
    construct_project(user_data)
    install(user_data, check=False)
    git_setup(user_data, check=False)