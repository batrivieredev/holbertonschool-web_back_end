#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension.
"""

from typing import List
# Importing the async_generator from the previous module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an asynchronous comprehension.
    """
    return [num async for num in async_generator()]  # Collects numbers asynchronously from async_generator

    """random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]  # Uncomment this line if needed to slice the list"""
