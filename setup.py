
from setuptools import find_packages, setup
from typing import List


# This is a function to get the list of requirements from the requirements.txt file

def get_requirements(file_path:str) -> list[str]:

    """
    This function will return the list of requirements
    """

    requirements = []

    # reading the requirements.txt file

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    # if -e . is present, then remove it

        if '-e .' in requirements:
            requirements.remove('-e .')


    return requirements




# Setup configuration for the project

setup(

    name='ML Project',
    version='0.1.0',
    author='Hariharan B',    
    author_email="hariharanbalasubramanian4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'), 

     
)