#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["Click>=7.0", "gtfparse>=1.2.1"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="João Vitor F. Cavalcante",
    author_email="jvfecav@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A simple utility CLI to convert GTF features to BED files",
    entry_points={
        "console_scripts": [
            "gtf2bed=gtf2bed.main:gtf2bed",
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="gtf2bed",
    name="gtf2bed",
    packages=find_packages(include=["gtf2bed", "gtf2bed.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jvfe/gtf2bed",
    version="0.1.0",
    zip_safe=False,
)
