#!/usr/bin/env python3
"""Module avec annotations de type qui fait la somme d'une liste de nombres flottants."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Fait la somme d'une liste de nombres à virgule flottante et retourne le résultat."""
    return sum(input_list)

