from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field


@dataclass
class Task:
    """Task stored in the priority queue.

    Tasks are ordered by `priority`, and tasks with the same priority are
    ordered by `insertion_order`.
    """

    name: str
    priority: int
    insertion_order: int = field(default=-1, repr=False, compare=False)


class PriorityQueue:
    """
    Stable binary min-priority queue of tasks.

    Lower numbers mean higher priority. Tasks with the same priority are
    returned in the order they were inserted.

    Operations:
        - heapify: O(n)
        - peek: O(1)
        - enqueue: O(log n)
        - dequeue: O(log n)
        - is_heap: O(n)
    """

    def __init__(self, tasks: list[Task] | None = None) -> None:
        """
        Build a priority queue from a list of tasks.

        The provided tasks are copied into the internal array and assigned an
        insertion order based on their input position.

        Args:
            tasks: Initial tasks to store in the queue.
        """

        self._heap = tasks.copy() if tasks else []

        for i, task in enumerate(self._heap):
            task.insertion_order = i

        self._next_insertion_order = len(self._heap)
        self._heapify()

    def __len__(self) -> int:
        """Return the number of tasks currently stored in the queue."""

        return len(self._heap)

    def __iter__(self) -> Iterator[Task]:
        """Iterate over the underlying heap array representation."""

        yield from self._heap

    def __repr__(self) -> str:
        """Return the debug representation of the queue."""

        return f"PriorityQueue({self._heap!r})"

    def __str__(self) -> str:
        """Return the string representation of the queue."""

        return repr(self)

    def __bool__(self) -> bool:
        """Return whether the queue contains at least one task."""

        return bool(self._heap)

    def __contains__(self, task: Task) -> bool:
        """Return whether a task is present in the queue."""

        return task in self._heap

    @staticmethod
    def _parent(index: int) -> int:
        """Return the parent index for a node in the heap array."""

        return (index - 1) // 2

    @staticmethod
    def _left_child(index: int) -> int:
        """Return the left child index for a node in the heap array."""

        return 2 * index + 1

    @staticmethod
    def _right_child(index: int) -> int:
        """Return the right child index for a node in the heap array."""

        return 2 * index + 2

    @staticmethod
    def _compare(task1: Task, task2: Task) -> bool:
        """
        Return whether task1 has higher priority than task2.

        Tasks are ordered first by priority and then by insertion order.

        Time Complexity:
            O(1)
        """

        return (task1.priority, task1.insertion_order) < (
            task2.priority,
            task2.insertion_order,
        )

    def _heapify(self) -> None:
        """
        Restore the heap property for the entire internal array.

        Time Complexity:
            O(n)
        """

        if not self._heap:
            return

        max_non_leaf = len(self._heap) // 2 - 1

        for index in range(max_non_leaf, -1, -1):
            self._bubble_down(index)

    def _bubble_up(self, index: int) -> None:
        """
        Restore the heap property by moving a node toward the root.

        Time Complexity:
            O(log n)
        """

        while index > 0:
            parent = self._parent(index)

            if self._compare(self._heap[index], self._heap[parent]):
                self._heap[index], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[index],
                )
                index = parent
            else:
                break

    def _bubble_down(self, index: int) -> None:
        """
        Restore the heap property by moving a node toward the leaves.

        Time Complexity:
            O(log n)
        """

        while True:
            best = index

            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self) and self._compare(self._heap[left], self._heap[best]):
                best = left

            if right < len(self) and self._compare(self._heap[right], self._heap[best]):
                best = right

            if best == index:
                break

            self._heap[index], self._heap[best] = (
                self._heap[best],
                self._heap[index],
            )

            index = best

    def enqueue(self, task: Task) -> None:
        """
        Insert a task into the queue.

        Args:
            task: The task to be inserted.

        Time Complexity:
            O(log n)
        """

        task.insertion_order = self._next_insertion_order
        self._next_insertion_order += 1
        self._heap.append(task)
        self._bubble_up(len(self) - 1)

    def dequeue(self) -> Task:
        """
        Remove and return the highest-priority task from the queue.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity:
            O(log n)
        """

        if not self._heap:
            raise IndexError("dequeue from empty queue")

        if len(self._heap) == 1:
            return self._heap.pop()

        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]

        highest_priority_task = self._heap.pop()
        self._bubble_down(0)

        return highest_priority_task

    def peek(self) -> Task:
        """
        Return the highest-priority task without removing it.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity:
            O(1)
        """

        if not self._heap:
            raise IndexError("peek from empty queue")

        return self._heap[0]

    def is_heap(self) -> bool:
        """
        Return whether the internal array satisfies the heap property.

        Time Complexity:
            O(n)
        """

        if not self._heap:
            return True

        max_non_leaf = len(self._heap) // 2 - 1

        for index in range(max_non_leaf + 1):
            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self) and self._compare(self._heap[left], self._heap[index]):
                return False

            if right < len(self) and self._compare(
                self._heap[right], self._heap[index]
            ):
                return False

        return True

    def is_empty(self) -> bool:
        """
        Return whether the queue contains no tasks.

        Time Complexity:
            O(1)
        """

        return not self._heap

    def clear(self) -> None:
        """
        Remove all tasks from the queue.

        Time Complexity:
            O(1)
        """

        self._heap = []
