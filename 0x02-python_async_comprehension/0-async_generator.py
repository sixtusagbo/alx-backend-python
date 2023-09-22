#!/usr/bin/env python3
"""Coroutine that yields random numbers"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Yields random integer between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
