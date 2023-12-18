from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:       ##here we are reading the file
        requirements=file_obj.readlines()  ## here we are reading the files from the file and storing it in the list
        requirements=[req.replace('/n',"") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

        
        
        
    


setup(
name='MLproject-end-to-end',
version='0.0.1',
author='Amit',
author_email='amitrathore110409@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)

###'''install_requires=['pandas','numpy','seaborn'], this way is not good in this we are wrting each and every thing which we want that package in our project but we don't want to do this so we are now maiking a function for this so that function take list from requirment.txt and return it to install_requires'''