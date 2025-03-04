from setuptools import find_packages,setup
from typing import List

hiphen_dot= '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n'," ") for req in requirements]

        if hiphen_dot in requirements:
            requirements.remove(hiphen_dot)


    return requirements
setup(
    name="diamond_price_prediction",  # Name of your project
    version="0.0.1",
    author='Rishabh Duta',
    author_email='rishabhdutta83@gmail.com',
    packages=find_packages(),  # Automatically find all packages
    install_requires=get_requirements('requirements.txt')
)