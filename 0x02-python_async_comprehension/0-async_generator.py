#!/usr/bin/env python3
""" Async Generators """


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator:
        This function returns an async generator
    """
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
