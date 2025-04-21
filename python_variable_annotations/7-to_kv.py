#!/usr/bin/env python3
"""
Module avec annotations de type qui prend
une chaîne de caractères k et un entier ou nombre flottant v comme arguments
et retourne un tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Retourne un tuple contenant la chaîne et le carré du nombre."""
    return (k, v * v)

