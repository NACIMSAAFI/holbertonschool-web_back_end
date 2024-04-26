#!/usr/bin/env python3
""" Program use python variabe annotations"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
