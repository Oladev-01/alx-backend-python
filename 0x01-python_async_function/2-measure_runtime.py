#!/usr/bin/env python3
"""awaiting"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return the run time/n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time() - start
    return elapsed / n
