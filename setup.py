from setuptools import find_packages
from setuptools import setup
from typing import List

PROJECT_NAME = "Flight Price Prediction"
VERSION = "0.0.1"
DESCRIPTION = "This is a project for predicting the price of the flight based on other features."
AUTHOR_NAME = "Ali Farid Khan"
AUTHOR_EMAIL = "alifaridkhan313@gmail.com"


REQ_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = "-e ."

###open --> read --> return 


def get_requirements_list() -> List[str]:
    with open(REQ_FILE_NAME) as requirement_file:
        req_list = requirement_file.readlines()
        req_list = [req_name.replace("\n", "") for req_name in req_list]

        if HYPHEN_E_DOT in req_list: 
            req_list.remove(HYPHEN_E_DOT)

        return req_list


setup(
    
    name = PROJECT_NAME, 
    version = VERSION, 
    description = DESCRIPTION, 
    author = AUTHOR_NAME, 
    author_email = AUTHOR_EMAIL, 
    packages = find_packages(), 
    install_requirements = get_requirements_list()

)