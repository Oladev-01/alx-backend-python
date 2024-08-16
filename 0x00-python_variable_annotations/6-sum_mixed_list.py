#!/usr/bin/env python3
"""union of types"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """mixed type sum"""
    return sum(mxd_lst)
