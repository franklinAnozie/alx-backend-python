#!/usr/bin/env python3
""" Async Comprehension """


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async comprehension:
        this function return a list comprehension
    """
    return [num async for num in async_generator()]
