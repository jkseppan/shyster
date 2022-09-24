# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_hyphenation.ipynb.

# %% auto 0
__all__ = ['hyphenator']

# %% ../02_hyphenation.ipynb 3
import re
import itertools as it
from collections.abc import Sequence, Mapping, Callable

# %% ../02_hyphenation.ipynb 5
def add_hyphens(
    s: str,  # word to hyphenate
    positions: Sequence[int],  # positions to insert hyphens (increasing order)
    hyphen: str='-'  # hyphen character
) -> str:  # word with hyphens
    i0, i1 = it.tee(iter(positions))
    i0 = it.chain((0,), i0)
    i1 = it.chain(i1, (len(s),))
    substrings = (s[p0:p1] for (p0,p1) in zip(i0, i1))
    return hyphen.join(substrings).strip(hyphen)

# %% ../02_hyphenation.ipynb 9
def hyphenator(
    regex: re.Pattern,  # first return value from `pattern.convert_patterns`
    mapping: Mapping[str, str],  # second return value from `pattern.convert_patterns`
    exceptions: Mapping[str, str],  # return value from `pattern.convert_exceptions`
    hyphen: str='-', # hyphen character
    lefthyphenmin: int=2,  # at least this many characters before the first hyphen
    righthyphenmin: int=3,  # at least this many characters after the last hyphen
) -> Callable[[str], str]:  # function that hyphenates words
    def fun(word):
        if (result := exceptions.get(word)):
            return result
        word = f'\x1f{word}\x1f'
        weights = bytearray(len(word))
        for match in regex.finditer(word):
            pos = match.span()[0]-1
            key = match.group(1)
            rule = mapping[key]
            for i, w in enumerate(rule):
                weights[pos+i] = max(weights[pos+i], w)
        positions = (i for (i,w) in enumerate(weights)
                     if w&1==1 and i>=lefthyphenmin and i<=len(word)-2-righthyphenmin)
        return add_hyphens(word[1:-1], positions, hyphen=hyphen)
    return fun
