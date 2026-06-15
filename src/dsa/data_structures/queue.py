from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    next: _Node | None = None


class Queue:
    """
    FIFO queue implementation internally connected using nodes.

    Linked structure that stores both head and tail pointers to support
    queueing and dequeueing in constant time.

    Operations:
        - enqueue: O(1)
        - dequeue: O(1)
        - peek: O(1)
        - is_empty: O(1)
        - clear: O(1)
    """

    def __init__(self, values: list[int] | None = None) -> None:
        """
        Build a queue from a list of integers.

        If no values are provided, an empty queue is created.

        Args:
            values: initial values to populate the queue.
        """

        if not values:
            self.head = None
            self.tail = None
            return

        node = _Node(values[0])
        self.head = node

        for value in values[1:]:
            new_node = _Node(value)
            node.next = new_node
            node = new_node

        self.tail = node

    def __len__(self) -> int:
        """
        Return number of elements in the queue.

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
        Traverse the queue from the first enqueued element to the last.

        Time Complexity:
            O(n)
        """

        node = self.head

        while node:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return f"Queue(out <- {list(self)} <- in)"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        return self.head is not None

    def enqueue(self, value: int) -> None:
        """
        Insert an element at the end of the queue.

        Args:
            value: element to be inserted.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            new_node = _Node(value)
            self.head = new_node
            self.tail = new_node
            return

        assert self.tail is not None
        self.tail.next = _Node(value)
        self.tail = self.tail.next

    def dequeue(self) -> int:
        """
        Return and remove the first element in the queue.

        Raises:
            IndexError: if the queue is empty.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            raise IndexError("dequeue from empty queue")

        value = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return value

    def peek(self) -> int:
        """
        Return the first element in the queue without removing it.

        Raises:
            IndexError: if the queue is empty.

        Time Complexity:
            O(1)
        """

        if self.head is None:
            raise IndexError("peek from empty queue")

        return self.head.value

    def is_empty(self) -> bool:
        """
        Return whether the queue is empty or not.

        Time Complexity:
            O(1)
        """

        return not self

    def clear(self) -> None:
        """
        Remove all elements from the queue.

        Time Complexity:
            O(1)
        """

        self.head = None
        self.tail = None
