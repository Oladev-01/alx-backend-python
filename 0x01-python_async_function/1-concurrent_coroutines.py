#!/usr/bin/env python3
"""awaiting"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of float of the delay times in sorted order"""
    delays = []  # for the list of delay times/sorted

    # we go n times, calling the wait_random to return delay time:
    for _ in range(n):
        delay = await wait_random(max_delay)  # getting delay time
        # next, we make sure to insert into the list a sorted order of times
        insert_idx = 0
        while insert_idx < len(delays) and delays[insert_idx] < delay:
            insert_idx += 1
        delays.insert(insert_idx, delay)
    return delays
