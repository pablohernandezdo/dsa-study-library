from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    next: _Node | None = None


class LinkedList:
    """
    A singly linked list of integers.

    Elements are stored in nodes connected through next references.
    This implementation only stores the head pointer.

    Operations:
        - insert_front: O(1)
        - insert_back: O(n)
        - find: O(n)
        - delete: O(n)
        - clear: O(1)
    """

    def __init__(self, values: list[int] | None = None) -> None:
        """
        Build a linked list from a list of integers.

        If no values are passed an empty linked list is created.

        Args:
            values: Initial values to populate the list.
        """
        if not values:
            self.head = None
            return

        self.head = _Node(values[0])
        prev = self.head

        for value in values[1:]:
            prev.next = _Node(value)
            prev = prev.next

    def __len__(self) -> int:
        """
        Return the number of elements in the list.

        Time Complexity:
            O(n)
        """
        length = 0
        node = self.head

        while node:
            length += 1
            node = node.next

        return length

    def __iter__(self) -> Iterator[int]:
        """
        Iterate over the values of the list from head to tail.

        Time Complexity:
            O(n)
        """
        node = self.head

        while node:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return f"LinkedList({list(self)})"

    def __str__(self) -> str:

        representation: str = ""

        for idx, value in enumerate(self):
            if idx == 0:
                representation += str(value)
            else:
                representation += f" -> {value}"

        return representation

    def insert_front(self, value: int) -> None:
        """
        Insert a value at the beginning of the list.

        Args:
            value: The value to be inserted.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            self.head = _Node(value)
        else:
            self.head = _Node(value, self.head)

    def insert_back(self, value: int) -> None:
        """
        Insert a value at the end of the list.

        Args:
            value: The value to be inserted.

        Time Complexity:
            O(n)
        """
        if self.head is None:
            self.head = _Node(value)
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = _Node(value)

    def find(self, value: int) -> int:
        """
        Return the index of the first occurrence of a value in the list.

        Args:
            value: Value to be found.

        Returns:
            The zero-based index of the value.

        Raises:
            ValueError: If the value is not present in the list.

        Time Complexity:
            O(n)
        """
        idx = 0
        node = self.head

        while node:
            if node.value == value:
                return idx

            idx += 1
            node = node.next

        raise ValueError(f"{value} is not in list")

    def delete(self, value: int) -> None:
        """
        Remove the first occurrence of value from the list.

        If the value is not present, the list is left unchanged.

        If value appears multiple times, only the first occurrence is removed.

        Args:
            value: Value to be deleted

        Time Complexity:
            O(n)
        """

        if self.head is None:
            return

        prev = None
        current = self.head

        while current:
            if current.value == value:
                if prev is None:
                    self.head = current.next

                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

    def clear(self) -> None:
        """
        Remove all elements from the list.

        Time Complexity:
            O(1)
        """
        self.head = None
