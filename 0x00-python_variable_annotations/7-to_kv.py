#!/usr/bin/env python3
"""mixed type"""

from typing import Union, Tuple


def to_kv(k: int, v: Union[int, float]) -> Tuple[str, float]:
    """mixed type"""
    return (k, (v ** 2))
