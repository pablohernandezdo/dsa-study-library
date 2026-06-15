from collections.abc import Iterator


class Stack:
    """
    LIFO (Last-In, First-Out) Stack implementation using Python's built-in list
    as the underlying dynamic array storage.

    Operations:
        - push O(1)
        - pop O(1)
        - peek O(1)
        - is_empty O(1)
        - clear O(1)
    """

    def __init__(self, values: list[int] | None = None) -> None:
        """
        Build a stack from a list of integers.

        The last element of the list represents the top of the stack.

        If no values are provided an empty stack is created.
        """

        self._items: list[int] = list(values) if values else []

    def __len__(self) -> int:
        """
        Return the number of values in the stack.

        Time Complexity:
            O(1)
        """
        return len(self._items)

    def __iter__(self) -> Iterator[int]:
        """
        Iterate from the top of the stack to the bottom.

        Time Complexity:
            O(n)
        """

        yield from reversed(self._items)

    def __reversed__(self) -> Iterator[int]:
        """
        Iterate from the bottom of the stack to the top.

        Time Complexity:
            O(n)
        """

        yield from self._items

    def __repr__(self) -> str:
        return f"Stack({self._items} <- top)"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        return bool(self._items)

    def push(self, value: int) -> None:
        """
        Insert an element at the top of the stack.

        Args:
            value: the element to be inserted.

        Time Complexity:
            O(1) amortized

        """
        self._items.append(value)

    def pop(self) -> int:
        """
        Remove the last inserted element to the stack.

        Raises:
            IndexError: if the stack is empty.

        Time Complexity:
            O(1) amortized
        """

        if not self._items:
            raise IndexError("pop from empty stack")

        return self._items.pop()

    def peek(self) -> int:
        """
        Return the last inserted element to the stack without removing it.

        Raises:
            IndexError: if stack is empty.

        Time Complexity:
            O(1)
        """

        if not self._items:
            raise IndexError("peek from empty stack")

        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Return whether the stack is empty or not.

        Time Complexity:
            O(1)
        """

        return not self._items

    def clear(self) -> None:
        """
        Remove all elements from the stack.

        Time Complexity:
            O(1)
        """

        self._items.clear()
