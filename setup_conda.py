from setuptools import setup, find_packages
import os
import sys


with open('LICENSE.txt', 'r', encoding='utf-8') as file:
    license_text = file.read()

name = "pybioportal"
version = "1.0.0"
description = "A Python package to easily retrieve data from cBioPortal."
author = "Matteo Valerio"
url = "https://github.com/Matteo-Valerio/pyBioPortal"
doc_url = "https://pybioportal.readthedocs.io"
license = license_text
keywords = "cBioPortal, API, bioinformatics"

install_requires = [
    "requests>=2.0.0",
    "pandas>=1.0.0",
    "numpy>=1.23.0"
]

packages = find_packages()

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    #author_email=author_email,
    url=url,
    project_urls={
        "Documentation": doc_url
    },
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    packages=packages,
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)