import os
from setuptools import setup, find_packages

with open("README.md","r") as f:
    long_description = f.read()


setup(
    name = "dotomorrow",
    version="0.0.1",
    description="A tool that allows users to interrupt for loops involving time-consuming evaluations, and resume the process during the next run.",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    packages= ['dotomorrow'],
    license="MIT",
    classifiers= [
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Widget Sets",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author="Teddy Chen",
    author_email="teddychenster@gmail.com",
    project_urls = {
        'github': "https://github.com/teddy21019/dotomorrow"
    },
)