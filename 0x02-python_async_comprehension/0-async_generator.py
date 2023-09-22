#!/usr/bin/python3
"""Coroutine that yields random numbers"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
