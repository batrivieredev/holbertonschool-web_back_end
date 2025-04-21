#!/usr/bin/env python3
"""Async task: create_task version of wait_random"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay and returns it."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a Task for wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))
