#!/usr/bin/env python3
"""This module is used to check my files"""

make_multiplier = __import__("8-make_multiplier").make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
