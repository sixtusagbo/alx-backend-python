#!/usr/bin/env python3
"""This module contains a function that converts its arguments to a
tuple of key-value pairs.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    return k, v * v
