from setuptools import find_packages,setup

def get_requirements():
    pass


setup(
    name="sensor",
    version="0.0.1",
    author="Anand",
    author_email="anandaluvala9391@gmail.com",
    package= find_packages(),
    install_requires=get_requirements(),
)