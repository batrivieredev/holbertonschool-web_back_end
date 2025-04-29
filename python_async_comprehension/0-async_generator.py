#!/usr/bin/env python3
"""
Module: 0-async_generator
This module contains an asynchronous generator coroutine that yields
10 random floats between 0 and 10, with a 1-second delay between each.
"""

import asyncio
import random
import typing


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10.

    Each value is yielded after a 1-second asynchronous wait.
    Returns:
        AsyncGenerator[float, None]: An async generator of 10 float values.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
