#!/usr/bin/env python3
"""Measure runtime for async comprehension operation"""
import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime for 4 async comprehension operations"""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    runtime = time.perf_counter() - start
    return runtime
