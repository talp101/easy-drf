#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of easy-drf.
# https://github.com/talp101/easy-drf.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Tal Peretz <13@1500.co.il>

from setuptools import setup, find_packages
from easy_drf import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='easy-drf',
    version=__version__,
    description='Django Rest Framework Become Easy',
    long_description='''
Django Rest Framework Become Easy
''',
    keywords='django djangorestframework',
    author='Tal Peretz',
    author_email='13@1500.co.il',
    url='https://github.com/talp101/easy-drf.git',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'djangorestframework>=2.3.5'
    ],
    extras_require={
        'tests': tests_require,
    },
)
