from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Self


class Heap(ABC):
    """
    Abstract binary heap of integers.

    Elements are stored in a zero-based array representation. Concrete
    subclasses define the ordering rule by implementing `_compare`.

    Operations:
        - heapify: O(n)
        - heapsort: O(n log n)
        - peek: O(1)
        - insert: O(log n)
        - extract: O(log n)
        - is_heap: O(n)
    """

    def __init__(self, heap: list[int] | None = None) -> None:
        """
        Build a heap from a list of integers.

        The provided values are copied into the internal array. The sequence
        is not heapified automatically.

        Args:
            heap: Initial values to store in the heap.
        """

        super().__init__()
        self._heap = heap.copy() if heap else []

    @abstractmethod
    def _compare(self, a: int, b: int) -> bool:
        """
        Return whether `a` should be above `b` in the heap ordering.
        """

    def __len__(self) -> int:
        return len(self._heap)

    def __iter__(self) -> Iterator[int]:
        yield from self._heap

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._heap})"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        return bool(self._heap)

    @staticmethod
    def parent(index: int) -> int:
        """Return the parent index for a node in the heap array."""

        return (index - 1) // 2

    @staticmethod
    def left_child(index: int) -> int:
        """Return the left child index for a node in the heap array."""

        return 2 * index + 1

    @staticmethod
    def right_child(index: int) -> int:
        """Return the right child index for a node in the heap array."""

        return 2 * index + 2

    @classmethod
    def heapify(cls, array: list[int]) -> Self:
        """
        Build a valid heap from a list of integers.

        Args:
            array: Values to arrange into a heap.

        Returns:
            A new heap instance of the concrete subclass.

        Time Complexity:
            O(n)
        """

        heap = cls(array)
        max_non_leaf = len(heap) // 2 - 1

        for index in range(max_non_leaf, -1, -1):
            heap._bubble_down(index)

        return heap

    @classmethod
    def heapsort(cls, array: list[int]) -> list[int]:
        """
        Return the values sorted according to the heap ordering.

        Args:
            array: Values to sort.

        Returns:
            A new sorted list.

        Time Complexity:
            O(n log n)
        """

        heap = cls.heapify(array)

        sorted_array: list[int] = []

        while heap:
            sorted_array.append(heap.extract())

        return sorted_array

    def _bubble_up(self, index: int) -> None:
        """
        Restore the heap property by moving a node toward the root.
        """

        while index > 0:
            parent = self.parent(index)

            if self._compare(self._heap[index], self._heap[parent]):
                (self._heap[index], self._heap[parent]) = (
                    self._heap[parent],
                    self._heap[index],
                )
                index = parent
            else:
                break

    def _bubble_down(self, index: int) -> None:
        """
        Restore the heap property by moving a node toward the leaves.
        """

        # which of the three nodes should be at the top ?

        while True:
            best = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < len(self) and self._compare(self._heap[left], self._heap[best]):
                best = left

            if right < len(self) and self._compare(self._heap[right], self._heap[best]):
                best = right

            if best == index:
                break

            self._heap[best], self._heap[index] = (
                self._heap[index],
                self._heap[best],
            )

            index = best

    def peek(self) -> int:
        """
        Return the root value without removing it.

        Raises:
            IndexError: If the heap is empty.

        Time Complexity:
            O(1)
        """

        if not self._heap:
            raise IndexError("peek from empty heap")

        return self._heap[0]

    def insert(self, value: int) -> None:
        """
        Insert a value into the heap.

        Args:
            value: The value to be inserted.

        Time Complexity:
            O(log n)
        """

        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def extract(self) -> int:
        """
        Remove and return the root value from the heap.

        Raises:
            IndexError: If the heap is empty.

        Time Complexity:
            O(log n)
        """

        if not self._heap:
            raise IndexError("extract from empty heap")

        if len(self._heap) == 1:
            return self._heap.pop()

        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        root = self._heap.pop()
        self._bubble_down(0)

        return root

    def is_heap(self) -> bool:
        """
        Return whether the internal array satisfies the heap property.

        Time Complexity:
            O(n)
        """

        if not self._heap:
            return True

        max_non_leaf = len(self) // 2 - 1

        for index in range(max_non_leaf + 1):
            left = self.left_child(index)
            right = self.right_child(index)

            if left < len(self._heap) and self._compare(
                self._heap[left], self._heap[index]
            ):
                return False

            if right < len(self._heap) and self._compare(
                self._heap[right], self._heap[index]
            ):
                return False

        return True


class MinHeap(Heap):
    """
    Binary min-heap of integers.

    The smallest value is kept at the root.
    """

    def _compare(self, a: int, b: int) -> bool:
        return a < b

    def extract_min(self) -> int:
        """
        Remove and return the minimum value from the heap.
        """

        return self.extract()


class MaxHeap(Heap):
    """
    Binary max-heap of integers.

    The largest value is kept at the root.
    """

    def _compare(self, a: int, b: int) -> bool:
        return a > b

    def extract_max(self) -> int:
        """
        Remove and return the maximum value from the heap.
        """

        return self.extract()
