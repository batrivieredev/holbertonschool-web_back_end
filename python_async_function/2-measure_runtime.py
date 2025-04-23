#!/usr/bin/env python3
"""Measure the runtime of wait_n"""
import time
from asyncio import run
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n and returns total_time / n."""
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
