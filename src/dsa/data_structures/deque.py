from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    prev: _Node | None = None
    next: _Node | None = None


class Deque:
    """
    Double-Ended Queue (deque) implemented as a doubly linked list of nodes.

    Operations:
        - append_left O(1)
        - append_right O(1)
        - pop_left O(1)
        - pop_right O(1)
        - peek_left O(1)
        - peek_right O(1)
        - is_empty O(1)
        - clear O(1)
    """

    def __init__(self, values: list[int] | None = None) -> None:
        """
        Build a deque by passing a list of integers. The first element of the list
        is inserted at the left end of the deque.

        Args:
            values: list of values to populate the deque with.
        """

        if not values:
            self.head = None
            self.tail = None
            return

        self.head = _Node(values[0])
        current = self.head

        for value in values[1:]:
            current.next = _Node(value, current)
            current = current.next

        self.tail = current

    def __len__(self) -> int:
        """
        Number of elements in the deque.

        Time Complexity:
            - O(n)
        """

        length = 0
        node = self.head

        while node:
            length += 1
            node = node.next

        return length

    def __iter__(self) -> Iterator[int]:
        """
        Iterate over the deque from left to right.

        Time Complexity:
            - O(n)
        """

        node = self.head

        while node:
            yield node.value
            node = node.next

    def __reversed__(self) -> Iterator[int]:
        """
        Iterate over the deque from right to left.

        Time Complexity:
            - O(n)
        """

        node = self.tail

        while node:
            yield node.value
            node = node.prev

    def __repr__(self) -> str:
        return f"Deque(left -> {list(self)} <- right)"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        return self.head is not None

    def append_left(self, value: int) -> None:
        """
        Insert an element at the left end of the deque.

        Args:
            value: the element to be inserted.

        Time Complexity:
            - O(1)
        """

        if self.head is None:
            self.head = _Node(value)
            self.tail = self.head
            return

        new_node = _Node(value, None, self.head)
        self.head.prev = new_node
        self.head = new_node

    def append_right(self, value: int) -> None:
        """
        Insert an element at the right end of the deque.

        Args:
            value: the element to be inserted.

        Time Complexity:
            - O(1)
        """

        if self.tail is None:
            self.head = _Node(value)
            self.tail = self.head
            return

        new_node = _Node(value, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self) -> int:
        """
        Return and remove the element at the left end of the deque.

        Raises:
            IndexError: if the deque is empty.

        Time Complexity:
            - O(1)
        """

        if self.head is None:
            raise IndexError("pop left from empty deque")

        value = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            assert self.head.next is not None
            self.head.next.prev = None
            self.head = self.head.next

        return value

    def pop_right(self) -> int:
        """
        Return and remove the element at the right end of the deque.

        Raises:
            IndexError: if the deque is empty.

        Time Complexity:
            - O(1)
        """

        if self.tail is None:
            raise IndexError("pop right from empty deque")

        value = self.tail.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            assert self.tail.prev is not None
            self.tail.prev.next = None
            self.tail = self.tail.prev

        return value

    def peek_left(self) -> int:
        """
        Return element at the left end of the deque without removing it.

        Raises:
            IndexError: if the deque is empty.

        Time Complexity:
            - O(1)
        """

        if not self.head:
            raise IndexError("peek left from empty deque")

        return self.head.value

    def peek_right(self) -> int:
        """
        Return element at the right end of the deque without removing it.

        Raises:
            IndexError: if the deque is empty.

        Time Complexity:
            - O(1)
        """

        if not self.tail:
            raise IndexError("peek right from empty deque")

        return self.tail.value

    def is_empty(self) -> bool:
        """
        Return whether the deque is empty or not.

        Time Complexity:
            - O(1)
        """

        return self.head is None

    def clear(self) -> None:
        """
        Remove all elements from de deque.

        Time Complexity:
            - O(1)
        """

        self.head = None
        self.tail = None
