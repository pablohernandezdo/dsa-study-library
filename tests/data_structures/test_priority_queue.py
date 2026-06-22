import pytest

from dsa.data_structures.priority_queue import PriorityQueue, Task


def get_non_empty_priority_queue() -> PriorityQueue:
    tasks = [
        Task("make the bed", 1),
        Task("have breakfast", 2),
        Task("walk the dog", 3),
    ]
    return PriorityQueue(tasks)


def test_initial_size_empty_priority_queue() -> None:
    pq = PriorityQueue()
    assert len(pq) == 0


def test_initial_size_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    assert len(pq) == 3


def test_build_non_empty_priority_queue_orders_by_priority() -> None:
    pq = PriorityQueue(
        [
            Task("walk the dog", 3),
            Task("have breakfast", 2),
            Task("make the bed", 1),
        ]
    )

    assert pq.dequeue() == Task("make the bed", 1)
    assert pq.dequeue() == Task("have breakfast", 2)
    assert pq.dequeue() == Task("walk the dog", 3)
    assert pq.is_empty()


def test_build_equal_priorities_queue_is_stable() -> None:
    pq = PriorityQueue(
        [
            Task("make the bed", 1),
            Task("have breakfast", 1),
            Task("walk the dog", 1),
        ]
    )

    assert pq.dequeue() == Task("make the bed", 1)
    assert pq.dequeue() == Task("have breakfast", 1)
    assert pq.dequeue() == Task("walk the dog", 1)
    assert pq.is_empty()


def test_len_mutation_priority_queue() -> None:
    pq = PriorityQueue()

    assert len(pq) == 0

    pq.enqueue(Task("make the bed", 1))
    pq.enqueue(Task("have breakfast", 2))
    pq.enqueue(Task("walk the dog", 3))

    assert len(pq) == 3

    pq.dequeue()
    assert len(pq) == 2

    pq.dequeue()
    assert len(pq) == 1

    pq.dequeue()
    assert len(pq) == 0


def test_iter_empty_priority_queue_protocol() -> None:
    pq = PriorityQueue()
    iterator = iter(pq)

    with pytest.raises(StopIteration):
        next(iterator)


def test_iter_non_empty_priority_queue_smoke() -> None:
    pq = get_non_empty_priority_queue()
    assert sum(1 for _ in pq) == len(pq)


def test_repr_empty_priority_queue() -> None:
    pq = PriorityQueue()
    assert repr(pq) == "PriorityQueue([])"


def test_repr_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    queue_repr = repr(pq)

    assert queue_repr.startswith("PriorityQueue([")
    assert queue_repr.endswith("])")
    assert "Task(name='make the bed', priority=1)" in queue_repr
    assert "Task(name='have breakfast', priority=2)" in queue_repr
    assert "Task(name='walk the dog', priority=3)" in queue_repr


def test_str_empty_priority_queue() -> None:
    pq = PriorityQueue()
    assert str(pq) == "PriorityQueue([])"


def test_str_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    assert str(pq) == repr(pq)


def test_bool_empty_priority_queue() -> None:
    pq = PriorityQueue()
    assert not pq


def test_bool_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    assert pq


def test_contains_empty_priority_queue() -> None:
    pq = PriorityQueue()
    task = Task("drink water", 1)
    assert task not in pq


def test_contains_existing_task() -> None:
    pq = get_non_empty_priority_queue()
    task = Task("make the bed", 1)
    assert task in pq


def test_contains_non_existing_task() -> None:
    pq = get_non_empty_priority_queue()
    task = Task("drink water", 1)
    assert task not in pq


def test_enqueue_empty_priority_queue() -> None:
    pq = PriorityQueue()
    task = Task("drink water", 1)

    pq.enqueue(task)

    assert len(pq) == 1
    assert pq.peek() == task
    assert pq.is_heap()


def test_enqueue_non_empty_priority_queue_preserves_stability() -> None:
    pq = get_non_empty_priority_queue()
    task = Task("drink water", 1)

    pq.enqueue(task)

    assert len(pq) == 4
    assert pq.is_heap()

    assert pq.dequeue() == Task("make the bed", 1)
    assert pq.dequeue() == Task("drink water", 1)
    assert pq.dequeue() == Task("have breakfast", 2)
    assert pq.dequeue() == Task("walk the dog", 3)
    assert pq.is_empty()


def test_dequeue_empty_priority_queue() -> None:
    pq = PriorityQueue()

    with pytest.raises(IndexError, match="dequeue from empty queue"):
        pq.dequeue()


def test_dequeue_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()

    first = pq.peek()
    task = pq.dequeue()

    assert task == first
    assert task == Task("make the bed", 1)
    assert len(pq) == 2


def test_dequeue_complete_queue() -> None:
    pq = get_non_empty_priority_queue()

    task1 = pq.dequeue()
    task2 = pq.dequeue()
    task3 = pq.dequeue()

    assert task1 == Task("make the bed", 1)
    assert task2 == Task("have breakfast", 2)
    assert task3 == Task("walk the dog", 3)
    assert len(pq) == 0


def test_enqueue_after_dequeuing_last_task() -> None:
    pq = get_non_empty_priority_queue()

    assert pq.dequeue() == Task("make the bed", 1)
    assert pq.dequeue() == Task("have breakfast", 2)
    assert pq.dequeue() == Task("walk the dog", 3)
    assert len(pq) == 0

    task = Task("drink water", 1)
    pq.enqueue(task)

    assert len(pq) == 1
    assert pq.peek() == task
    assert pq.dequeue() == task
    assert pq.is_empty()


def test_peek_empty_queue() -> None:
    pq = PriorityQueue()

    with pytest.raises(IndexError, match="peek from empty queue"):
        pq.peek()


def test_peek_non_empty_queue() -> None:
    pq = get_non_empty_priority_queue()

    peek_task = pq.peek()

    assert peek_task == Task("make the bed", 1)
    assert len(pq) == 3


def test_is_heap_heapified_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    assert pq.is_heap()


def test_is_heap_detects_invalid_internal_heap_state() -> None:
    pq = PriorityQueue()
    pq._heap = [  # type: ignore
        Task("walk the dog", 3, insertion_order=0),
        Task("make the bed", 1, insertion_order=1),
        Task("have breakfast", 2, insertion_order=2),
    ]
    assert not pq.is_heap()


def test_is_empty_empty_priority_queue() -> None:
    pq = PriorityQueue()
    assert pq.is_empty()


def test_is_empty_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()
    assert not pq.is_empty()


def test_clear_empty_priority_queue() -> None:
    pq = PriorityQueue()

    pq.clear()

    assert len(pq) == 0
    assert pq.is_empty()


def test_clear_non_empty_priority_queue() -> None:
    pq = get_non_empty_priority_queue()

    pq.clear()

    assert len(pq) == 0
    assert pq.is_empty()
