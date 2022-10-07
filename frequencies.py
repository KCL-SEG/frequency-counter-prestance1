from collections import Counter
from typing import Union, List, Dict

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items: List[Union[str, int]]) -> Dict[str, int]:
    return Counter(str(item) for item in items)
