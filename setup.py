#!/usr/bin/env python
"""
File: setup.py
Author: Keith Tauscher (updated)
Description: Installs pylinex.
"""
from setuptools import setup, find_packages

setup(
    name='pylinex',
    version='0.1',
    description='Linear signal extraction in Python',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'h5py',
    ],
)
