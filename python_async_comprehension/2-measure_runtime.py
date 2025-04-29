#!/usr/bin/env python3
"""
Module mesurant le temps d'exécution de plusieurs appels concurrents
à une coroutine asynchrone.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Lance quatre exécutions concurrentes de async_comprehension
    et mesure le temps total d'exécution.

    Retour :
        float : Temps d'exécution total en secondes.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
