from setuptools import find_packages, setup
from typing import List

ignore= '-e'

def get_requiremnts(file_path:str)->List[str]: # open file path as string and as a list
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if ignore in requirements:
            requirements.remove(ignore)

    return requirements

setup(
    name="dsproject",
    version='0.0.1',
    author_email='chetan061996@gmail.com',
    packages=find_packages(),
    install_requiremnts=get_requiremnts('requirements.txt')

)