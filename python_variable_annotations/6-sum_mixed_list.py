#!/usr/bin/env python3
"""
Module avec annotations de type qui prend une liste d'entiers et de nombres flottants
et retourne leur somme sous forme de float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Retourne la somme d'une liste d'entiers et de nombres

