#!/usr/bin/env python3
"""This module execute multiple coroutines at the same time with async"""
import asyncio
from typing import List, cast


random_number = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time"""
    delays = []
    for x in range(n):
        delay = await random_number(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return cast(List[float], delays)
