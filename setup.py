# !/usr/bin/env python3
# coding:utf-8
"""
Name       : setup.py
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description: Used to setup and publish
"""

from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
]

setup(
    name="google-colab-shell",
    version="0.1.1",
    description="An efficent python package to launch terminal in Google Colab",
    long_description=open("README.md").read()
    + "\n\n"
    + open("CHANGELOG.md").read()
    + "\n\nRead more at https://github.com/singhsidhukuldeep/Google-Colab-Shell",
    long_description_content_type="text/markdown",
    url="https://github.com/singhsidhukuldeep/Google-Colab-Shell",
    author="Kuldeep Singh Sidhu",
    author_email="singhsidhukuldeep@gmail.com",
    classifiers=classifiers,
    keywords="Google Colab Shell Terminal",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
)