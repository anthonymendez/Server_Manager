from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Server_Manager",
    version='0.0.2',
    author="Anthony Mendez",
    author_email="anthonymendez9@gmail.com",
    description="Server Manager is a Flask web application that allows you create or download plugins to view various statistics for your server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anthonymendez/Server_Manager",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires=">=3.8"
)