#!/usr/bin/env python3
"""Program use Asyncin in python"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """An async routine called wait_n that takes in
    2 int arguments (in this order):n and max_delay.
    Return the list of all the delays (float values)."""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
