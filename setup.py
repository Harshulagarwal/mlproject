from setuptools import find_packages, setup
from typing import List

DASH_E_DOT = '-e .'

def get_requirements(file_path) -> List[str]:
    '''
    returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]


        if DASH_E_DOT in requirements:
            requirements.remove(DASH_E_DOT)

    return requirements        


setup (
    name = 'mlproject',
    version = '0.0.1',
    author = 'harshul',
    author_email = 'harshulagarwal.98@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)