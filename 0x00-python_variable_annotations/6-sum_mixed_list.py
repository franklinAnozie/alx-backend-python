#!/usr/bin/env python3
""" type annotation: List """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    """ returns the sum of the arguments passed """
    sum: float = 0.00

    for num in mxd_lst:
        sum += num

    return sum
