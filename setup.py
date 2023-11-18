from setuptools import find_packages,setuptools
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.place("\n","")for req in requirements]

        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = 'Segmentation_Project',
    version = 0.0.1,
    author = 'Anant'
    author_email = 'anantsingh.abhinav@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)