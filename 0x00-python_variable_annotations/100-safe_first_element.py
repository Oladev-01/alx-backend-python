#!/usr/bin/env python3
"""sequence of any"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return any type"""
    if lst:
        return lst[0]
    else:
        return None
