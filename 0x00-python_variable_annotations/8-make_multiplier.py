#!/usr/bin/env python3
"""This module contians a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a multiplier function"""

    def worker(number: float) -> float:
        return multiplier * number

    return worker
