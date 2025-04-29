#!/usr/bin/env python3
"""
Ce module définit une coroutine asynchrone permettant de générer
des nombres aléatoires de manière non bloquante à l'aide d'asyncio.
"""

import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    Coroutine asynchrone qui produit 10 nombres flottants aléatoires.

    À chaque itération, la coroutine attend une seconde (sans bloquer
    l'exécution globale) avant de produire un nouveau nombre compris
    entre 0 et 10.

    Retour :
        AsyncGenerator[float, None] : Générateur asynchrone de nombres à virgule flottante.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
