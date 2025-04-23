#!/usr/bin/env python3
"""
This module defines an async function `task_wait_n` that creates
multiple asynchronous tasks using `task_wait_random`, and returns
the delays in the order of completion.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return the list of delays
    in the order of completion, without using sort().

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each call.

    Returns:
        List[float]: List of delays in the order they complete.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)
    return delays
