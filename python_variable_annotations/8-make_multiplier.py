#!/usr/bin/env python3
"""
Module avec annotations de type qui prend un multiplicateur de type float comme argument
et retourne une fonction qui multiplie un float par ce multiplicateur.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Retourne une fonction qui multiplie un nombre flottant par le multiplicateur."""
    def multiply(n: float) -> float:
        """Retourne le produit d'un nombre flottant et du multiplicateur."""
        return n * multiplier
    return multiply

