import setuptools


with open("Readme.md", 'r', encoding='utf-8') as f:
    long_description = f.read() 


__version__ = "0.0.0"
REPO_NAME = "Car-Parking-Counter"
AUTHOR_USER_NAME = "ishumann"
SRC_REPO = "carParkingCounter"
AUTHOR_EMAIL = "mann.agrawal17@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    discription="A small python package for Computer vision.",
    long_description= long_description,
    long_description_content= 'text/markdown',
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where='src')
    
)
