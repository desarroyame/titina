#!/usr/bin/env python3
"""
Setup configuration for the Titin Chemical Name Generator project
"""

from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements file
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="titin-chemical-name-generator",
    version="1.0.0",
    author="Titin Project",
    author_email="",
    description="Generador del nombre químico completo de la proteína titina",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "titin-generator=main:main",
            "titin-demo=demo:demo_chemical_name",
            "titin-utils=utils:main",
        ],
    },
    keywords="bioinformatics chemistry protein titin amino-acids",
    project_urls={
        "Documentation": "",
        "Source": "",
        "Tracker": "",
    },
)
