#!/usr/bin/env python3
""" type annotation: List """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns the sum of the arguments passed """
    return lambda multi: multi * multiplier
