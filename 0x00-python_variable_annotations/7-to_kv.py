#!/usr/bin/env python3
""" type annotation: List """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns the sum of the arguments passed """
    return (k, (v * v))
