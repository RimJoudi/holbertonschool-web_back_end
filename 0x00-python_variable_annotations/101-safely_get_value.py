#!/usr/bin/python3
"""
safely_get_value fn
"""
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None])\
                         -> Union[TypeVar('T'), None]:
    """
    safely_get_value fn
    """
    if key in dct:
        return dct[key]
    else:
        return default
