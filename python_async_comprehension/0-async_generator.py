#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator coroutine that generates 10 random numbers between 0 and 10.
    Each number is yielded after an asynchronous 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second before each generation
        yield random.uniform(0, 10)  # Yield a random floating-point number between 0 and 10
