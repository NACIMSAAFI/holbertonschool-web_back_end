#!/usr/bin/env python3
""" Program use python variabe annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the square of the int/float v."""
    return (k, float(v * v))
