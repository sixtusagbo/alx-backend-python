#!/usr/bin/env python3
"""Async comprehension from an async generator"""
import asyncio
from typing import List

agen = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[int]:
    """Async comprehend an async generator"""
    return [i async for i in agen()]
