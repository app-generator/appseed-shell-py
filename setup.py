import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
name='appseed-shell',
version='0.0.1',
zip_safe=False,
packages=find_packages(),
include_package_data=True,
description='Implements the Python interface to all services exposed by AppSeed',
long_description=README,
url='https://github.com/app-generator/appseed-shell-py',
author='AppSeed.us',
author_email='support@appseed.us',
license='MIT License',
classifiers=[
    'Environment :: System Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'Topic :: Software Development :: User Interfaces',
    ],
)