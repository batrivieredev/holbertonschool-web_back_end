#!/usr/bin/env python3
"""
Module qui récupère les valeurs produites par une coroutine asynchrone
en utilisant une compréhension asynchrone.
"""

from typing import List

# Importation dynamique de la coroutine du fichier précédent
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Exécute async_generator et collecte les valeurs dans une liste
    grâce à une compréhension asynchrone.

    Retour :
        List[float] : Liste de 10 nombres générés de manière asynchrone.
    """
    return [num async for num in async_generator()]
