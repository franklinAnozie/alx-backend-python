#!/usr/bin/env python3
""" python script to practice coroutines """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        takes an int value and sleeps for a random value of seconds
        between 0 and the value
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
