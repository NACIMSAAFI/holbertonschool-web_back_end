#!/usr/bin/env python3
"""Program use Asyncin in python"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns the list of all the task
    """
    delay_list = []
    for i in range(n):
        delay_list.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delay_list)]
