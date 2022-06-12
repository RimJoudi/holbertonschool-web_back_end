#!/usr/bin/env python3
"""
Annotating a function’s parameters
and it's return values with the appropriate types
"""


from typing import Iterable, List, Sequence, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotating a function’s parameters
    and it's return values with the appropriate types
    """

    return [(i, len(i)) for i in lst]
