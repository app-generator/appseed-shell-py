#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cookiecutter.main import cookiecutter

__test__ = {'import_test': """
                           >>> from appseed_shell.submodule import *

                           """}

def hello():
    """
    Function description

    Example/s of use (and excutable test/s via doctest):
    >>> func_create_file("file.txt")
    'line in file'

    :param path_to_file: set a path to file
    :return: string with first line in file
    """

    return "AppSeed Python CLI"

def generate_django():
    cookiecutter('https://github.com/app-generator/cookiecutter-django.git')

__test__ = {
    'clean_test_files': """
                        >>> from pathlib import Path
                        >>> Path("file.txt").unlink()

                        """}
