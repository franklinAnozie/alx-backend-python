#!/usr/bin/env python3
""" Async Comprehension """


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure runtime function:
        This function measures the runtime of the comprehension
        when it tries to run the comprehension four times
        its always approximately 10secs
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for num in range(4)])
    return time.perf_counter() - start
