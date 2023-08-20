#!/usr/bin/env python3
"""This module execute multiple coroutines at the same time with async"""
from typing import List, cast


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time"""
    delays = []
    for x in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return cast(List[float], delays)
