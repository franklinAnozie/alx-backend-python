#!/usr/bin/env python3
""" more coroutines """

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        takes an int value and sleeps for a random value of seconds
        between 0 and the value
    """
    return asyncio.create_task(wait_random(max_delay))
