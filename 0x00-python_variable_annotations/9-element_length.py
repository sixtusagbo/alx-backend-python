#!/usr/bin/env python3
"""This module contains an annotated function that
returns info about an iterable"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
