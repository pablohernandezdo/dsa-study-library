from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    prev: _Node | None = None
    next: _Node | None = None


class DoublyLinkedList:
    """
    A doubly linked list of integers.

    Elements are stored in nodes connected through references to the previous
    and next nodes. This implementation stores both the head and tail pointers.

    Operations:
        - insert_front: O(1)
        - insert_back: O(1)
        - find: O(n)
        - delete: O(n)
        - clear: O(1)
        - pop_front: O(1)
        - pop_back: O(1)
    """

    def __init__(self, values: list[int] | None = None) -> None:
        """
        Build a doubly linked list from a list of integers.

        If no values are passed an empty list is created.

        Args:
            values: Initial values to populate the list.
        """

        if not values:
            self.head = None
            self.tail = None
            return

        self.head = _Node(values[0])
        current: _Node = self.head

        for value in values[1:]:
            current.next = _Node(value, current)
            current = current.next

        self.tail = current

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

    def __reversed__(self) -> Iterator[int]:
        """
        Iterate over the values of the list from tail to head.

        Time Complexity:
            O(n)
        """

        node = self.tail

        while node:
            yield node.value
            node = node.prev

    def __repr__(self) -> str:
        return f"DoublyLinkedList({list(self)})"

    def __str__(self) -> str:

        if self.head is None:
            return ""

        representation: str = ""

        for idx, value in enumerate(self):
            if idx == 0:
                representation += f"{value}"
            else:
                representation += f" <-> {value}"

        return representation

    def insert_front(self, value: int) -> None:
        """
        Insert a value at the beginning of the list.

        If the list is empty, the inserted node is assigned to both the head and tail.

        Args:
            value: The value to be inserted.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            node = _Node(value)
            self.head = node
            self.tail = node
            return

        new_node = _Node(value, None, self.head)
        self.head.prev = new_node
        self.head = new_node

    def insert_back(self, value: int) -> None:
        """
        Insert a value at the end of the list.

        If the list is empty, the inserted node is assigned to both the head and tail.

        Args:
            value: The value to be inserted.

        Time Complexity:
            O(1)
        """

        if self.tail is None:
            node = _Node(value)
            self.head = node
            self.tail = node
            return

        new_node = _Node(value, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node

    def find(self, value: int) -> int:
        """
        Return the index of the first occurrence of a value in the list, traversed from
        head to tail.

        Args:
            value: The value to search for.

        Returns:
            The zero-based index of the value's first occurrence.

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

        raise ValueError(f"{value} not found in list")

    def delete(self, value: int) -> None:
        """
        Delete the first occurrence of a value in the list.

        If the value is not present the list is left unchanged.

        If the value appears multiple times, only the first occurrence is removed.

        Args:
            value: The value to be removed.

        Time Complexity:
            O(n)
        """

        if self.head is None:
            return

        node: _Node | None = self.head

        while node:
            if node.value == value:
                # deleting head
                if node is self.head:
                    # head = tail
                    if self.head is self.tail:
                        self.head = None
                        self.tail = None

                    # other
                    else:
                        self.head = self.head.next

                        assert self.head is not None
                        self.head.prev = None

                # deleting tail
                elif node is self.tail:
                    assert self.tail is not None
                    assert self.tail.prev is not None

                    self.tail.prev.next = None
                    self.tail = self.tail.prev

                # deleting in the middle
                else:
                    assert node.prev is not None
                    assert node.next is not None

                    node.prev.next = node.next
                    node.next.prev = node.prev

                return

            node = node.next

    def clear(self) -> None:
        """
        Remove all nodes from the list.

        Time Complexity:
            O(1)
        """

        self.head = None
        self.tail = None

    def pop_front(self) -> int:
        """
        Remove the element at the head of the list.

        Returns:
            The value of the element at the head of the list.

        Raises:
            IndexError: If the list is empty.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            raise IndexError("pop from empty list")

        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        first_value: int = self.head.value

        assert self.head.next is not None
        self.head.next.prev = None
        self.head = self.head.next

        return first_value

    def pop_back(self) -> int:
        """
        Remove the element at the tail of the list.

        Returns:
            The value of the element at the tail of the list.

        Raises:
            IndexError: If the list is empty.

        Time Complexity:
            O(1)
        """

        if self.tail is None:
            raise IndexError("pop from empty list")

        if self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value

        last_value: int = self.tail.value

        assert self.tail.prev is not None
        self.tail.prev.next = None
        self.tail = self.tail.prev

        return last_value
