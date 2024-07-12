#!/usr/bin/env python3
""" measure time """


import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        takes an int value and sleeps for a random value of seconds
        between 0 and the value
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter() - start

    ret_val = end / n

    return ret_val
