#!/usr/bin/env python3
"""await task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creating an await task"""
    return asyncio.Task(wait_random(max_delay))
