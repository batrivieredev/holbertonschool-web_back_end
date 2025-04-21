#!/usr/bin/env python3
"""
Fonction annotée avec des types qui prend une liste mxd_lst d'entiers et de flottants
et retourne leur somme sous forme de float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Retourne la somme des éléments d'une liste contenant des entiers et des flottants."""
    return float(sum(mxd_lst))
