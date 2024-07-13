#!/usr/bin/env python3
""" type annotation: List """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of the arguments passed """
    sum: float = 0.00

    for num in input_list:
        sum += num

    return sum
