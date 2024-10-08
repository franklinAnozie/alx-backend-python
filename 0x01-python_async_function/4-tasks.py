#!/usr/bin/env python3
""" more coroutines """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        takes an int value and sleeps for a random value of seconds
        between 0 and the value
    """
    ret_val: List[float] = []
    n_ret_val: List[float] = []

    for num in range(n):
        ret_val.append(task_wait_random(max_delay))

    for num in asyncio.as_completed(ret_val):
        result = await num
        n_ret_val.append(result)

    return n_ret_val
