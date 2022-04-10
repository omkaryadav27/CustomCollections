from collections.abc import Sequence
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return (index != len(self._items)) and (self._items[index] == item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return f'SortedSet({self._items if self._items else ""})'

    def __eq__(self, other):
        if not isinstance(other, SortedSet): return NotImplemented

        return self._items == other._items

    def __ne__(self, other):
        if not isinstance(other, SortedSet): return NotImplemented

        return self._items != other._items

    def __add__(self, other):
        return SortedSet(chain(self, other))

    def __mul__(self, other):
        return self if other >= 1 else SortedSet()

    def __rmul__(self, other):
        return self * other

    def index(self, value) -> int:
        index = bisect_left(self._items, value)
        if (index != len(self._items)) and (self._items[index] == value):
            return index
        raise ValueError(f'{value} not found')

    def count(self, value) -> int:
        return int(value in self)


if __name__ == '__main__':
    pass
    # from random import randrange
    # s = SortedSet(randrange(1000) for _ in range(2000))
    # from timeit import timeit
    # timeit(setup='from __main__ import s',\
    #       stmt = '[s.count(i) for i in range(1000)]', number = 100)
