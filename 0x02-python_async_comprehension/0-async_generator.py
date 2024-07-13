#!/usr/bin/env python3
""" Async Generators """


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
