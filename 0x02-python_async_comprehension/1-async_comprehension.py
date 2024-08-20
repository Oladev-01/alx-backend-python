#!/usr/bin/env python3
"""yield async"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """yeild as comprehension"""
    ran = [ran async for ran in async_generator()]
    return ran
