#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


__test__ = {
    'clean_test_files': """
                        >>> from pathlib import Path
                        >>> Path("file.txt").unlink()

                        """}
