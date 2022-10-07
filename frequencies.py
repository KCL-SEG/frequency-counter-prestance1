from collections import Counter
from typing import Union, List, Mapping

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items: List[Union[str, int]]) -> Mapping[str, int]:
    return Counter(str(item) for item in items)
