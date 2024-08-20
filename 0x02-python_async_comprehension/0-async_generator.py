#!/usr/bin/env python3
"""yield async"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """yield async"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
