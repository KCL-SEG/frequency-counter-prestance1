from collections import Counter
from typing import Union, List, Dict

"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items: List[Union[str, int]]) -> Dict[str, int]:
    return dict(Counter(str(item) for item in items))

print(frequencies(['n', 'o', 'o', 'b']))