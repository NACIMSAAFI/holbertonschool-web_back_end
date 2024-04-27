#!/usr/bin/env python3
"""Program use async_comprehension in python"""

from typing import List
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    An async coroutine that uses async comprehension
    to collect 10 random numbers.
    """
    return [num async for num in async_generator()]
