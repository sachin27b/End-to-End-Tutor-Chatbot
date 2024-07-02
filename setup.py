from setuptools import find_packages, setup

setup(
    name = 'Chatbot',
    version= '0.0.0',
    author= 'Sachin Bahuleyan',
    author_email= 'sachin270895@gmail.com',
    packages= find_packages(), # find_package will look for __init__.py in all the folders and considers it as package
    install_requires = []

)

# after this run command "pip install -r requirements.txt", don't have to run setup.py