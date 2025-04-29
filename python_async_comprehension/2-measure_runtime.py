#!/usr/bin/env python3
"""
Module to measure the execution time of parallel tasks.
"""

import asyncio
import time

# Importing async_comprehension from the previous module
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the total execution time.
    """
    start_time = time.perf_counter()  # Start the timer
    await asyncio.gather(*(async_comprehension() for _ in range(4)))  # Execute 4 async_comprehension tasks in parallel
    return time.perf_counter() - start_time  # Return the elapsed time
