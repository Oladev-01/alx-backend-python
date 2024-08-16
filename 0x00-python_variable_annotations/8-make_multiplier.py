#!/usr/bin/env python3
"""float type annotation"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function"""
    def mult_float(value: float) -> float:
        """returning mul of val and multiplier"""
        return value * multiplier
    return mult_float
