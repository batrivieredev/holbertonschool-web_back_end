#!/usr/bin/env python3
"""
Annoter les paramètres et les valeurs de retour des fonctions ci-dessous avec les types appropriés
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Retourne une liste de tuples où le premier élément
    de chaque tuple passé est le tuple original
    et le second élément est la longueur du tuple.
    """
    return [(i, len(i)) for i in lst]

