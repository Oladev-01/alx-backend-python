#!/usr/bin/python3
"""waiting"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """awaiting a delay and return the delayed time(float)"""
    delayed_time = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_time)
    return delayed_time
