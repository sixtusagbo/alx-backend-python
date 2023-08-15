#!/usr/bin/env python3
"""This module contains a function that sums up a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of numbers"""
    sum = 0

    for num in input_list:
        sum += num

    return sum
