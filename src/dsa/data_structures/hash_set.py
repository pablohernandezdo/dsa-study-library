from __future__ import annotations

from collections.abc import Iterator

from dsa.data_structures.chaining_hash_map import HashMap


class HashSet:
    """
    Hash Set implementation based on chaining Hash Map.

    Every element of the Hash Set is stored as a key in the Hash Map with a value of 0.

    Operations:
        - add: average O(1), worst case O(n)
        - remove: average O(1), worst case O(n)
        - is_empty: O(1)
        - clear: O(1)
    """

    def __init__(self, values: list[str] | None = None) -> None:
        """
        Build a Hash Set from a list of strings.

        If no values are provided, an empty Hash Set is created.

        Args:
            values: the elements to populate the Hash Set.
        """

        self._hm = HashMap()

        if values:
            for value in values:
                self._hm.put(value, 0)

    def __len__(self) -> int:
        """
        Return the number of elements in the Hash Set.

        Time Complexity:
            - O(1)
        """

        return len(self._hm)

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over the elements of the Hash Set.

        Time Complexity:
            - O(n)
        """

        yield from self._hm

    def __repr__(self) -> str:
        items = sorted(repr(v) for v in self._hm)
        return f"HashSet({{{', '.join(items)}}})"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        return bool(self._hm)

    def __contains__(self, item: str) -> bool:
        return item in self._hm

    def add(self, value: str) -> None:
        """
        Add an element to the hash set.

        When adding an existing element the Hash Set remains unchanged.

        Args:
            value: the element to be inserted.

        Time Complexity:
            - Average O(1)
            - Worst case O(n)
        """

        self._hm.put(value, 0)

    def remove(self, value: str) -> None:
        """
        Remove an element from the Hash Set.

        Args:
            value: the element to be removed.

        Raises:
            KeyError: if the element is not present in the Hash Set.

        Time Complexity:
            - Average O(1)
            - Worst case O(n)
        """

        self._hm.remove(value)

    def is_empty(self) -> bool:
        """
        Return whether the Hash Set contains elements or not.

        Time Complexity:
            - O(1)
        """

        return not self

    def clear(self) -> None:
        """
        Remove all elements from the Hash Set.

        Time Complexity:
            - O(1)
        """

        self._hm = HashMap()
