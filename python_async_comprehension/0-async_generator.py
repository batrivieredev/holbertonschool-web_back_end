#!/usr/bin/env python3
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that yields a random float between 0 and 10, 10 times, waiting 1 second between each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
