#!/usr/bin/env python3
""" more coroutines """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        takes an int value and sleeps for a random value of seconds
        between 0 and the value
    """
    ret_val: list[float] = []
    n_ret_val: list[float] = []

    for num in range(n):
        ret_val.append(wait_random(max_delay))

    for num in asyncio.as_completed(ret_val):
        result = await num
        n_ret_val.append(result)

    return n_ret_val
