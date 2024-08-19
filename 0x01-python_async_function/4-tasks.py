#!/usr/bin/env python3
"""awaiting"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return list of float of the delay times in sorted order"""
    # we go n times, calling the wait_random to return delay time:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # next, we make sure to insert into the list a sorted order of times
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
