#!/usr/bin/env python3
"""This module is used to check my files"""

to_kv = __import__("7-to_kv").to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
