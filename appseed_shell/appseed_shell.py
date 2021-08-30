#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .submodule import hello
from .submodule import generate_django

__test__ = {'import_test': """
                           >>> from appseed_shell.appseed_shell import *

                           """}
