#!/usr/bin/env python3
"""Async tasks: execute wait_random concurrently using asyncio.create_task"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a Task that wraps wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return sorted delays (without sort())."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)
    return delays
