#!/usr/bin/env python3
"""Async waits for a random delay between 0 and max_delay seconds."""
import asyncio
from typing import List, Coroutine
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Async waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for the wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs task_wait_random coroutine n times with the specified max_delay"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
