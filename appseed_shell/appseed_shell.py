#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .submodule import hello

__test__ = {'import_test': """
                           >>> from appseed_shell.appseed_shell import *

                           """}


def func_of_my_module(arg_a, arg_b, kwarg_a=0, kwarg_b="Nothing"):
    """
    Function description

    Example/s of use (and excutable test/s via doctest):
    >>> func_of_my_module(123, "hello", kwarg_b="Something")
    'Something to return'

    >>> func_of_my_module(987, "bye")
    'Nothing to return'

    :param arg_a: arg description
    :param arg_b: arg description
    :param kwarg_a: arg description. By default: 0
    :param kwarg_b: arg description. By default: "Something"
    :return: one string
    """

    # My function content. Use: arg_a, arg_b, kwarg_a, kwarg_b ...
    hello()

    return "{} to return".format(kwarg_b)
