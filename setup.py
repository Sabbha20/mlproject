from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """ This function returns a list of requirements from a given file path."""
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[line.replace("\n", "") for line in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version="0.0.1",
    author="Sabbha",
    author_email="sabbha.power1@gmail.com",
    description="End to end Machine Learning Project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)