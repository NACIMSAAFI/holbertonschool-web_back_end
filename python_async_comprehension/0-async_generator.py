#!/usr/bin/env python3
"""Program use async_comprehension in python"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An async coroutine that yields random numbers
    10 times with a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
