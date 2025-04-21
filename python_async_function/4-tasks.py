#!/usr/bin/env python3
"""Async tasks: execute task_wait_random concurrently"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return delays sorted by completion order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)
    return delays
