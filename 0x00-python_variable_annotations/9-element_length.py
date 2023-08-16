#!/usr/bin/env python3
"""This module contains an annotated function that
returns info about a sequence"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return info about a sequence"""
    return [(i, len(i)) for i in lst]
