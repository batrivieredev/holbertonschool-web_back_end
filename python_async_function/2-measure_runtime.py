#!/usr/bin/env python3
"""Async waits for a random delay between 0 and max_delay seconds."""
import time
from typing import List
from asyncio import run
from asyncio import Task


async def wait_random(max_delay: int = 10) -> float:
    """Async waits for a random delay between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs wait_random coroutine n times with the specified max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)


def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n and returns total_time / n."""
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
