import pytest

from dsa.data_structures.queue import Queue


def test_build_empty_queue() -> None:
    queue = Queue()
    assert list(queue) == []


def test_build_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert list(queue) == [1, 2, 3]


def test_len_empty_queue() -> None:
    queue = Queue()
    assert len(queue) == 0


def test_len_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert len(queue) == 3


def test_iter_empty_queue() -> None:
    queue = Queue()
    assert list(queue) == []


def test_iter_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert list(queue) == [1, 2, 3]


def test_iter_is_repeatable() -> None:
    queue = Queue([1, 2, 3])

    assert list(queue) == [1, 2, 3]
    assert list(queue) == [1, 2, 3]


def test_repr_empty_queue() -> None:
    queue = Queue()
    assert repr(queue) == "Queue(out <- [] <- in)"


def test_repr_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert repr(queue) == "Queue(out <- [1, 2, 3] <- in)"


def test_str_empty_queue() -> None:
    queue = Queue()
    assert str(queue) == "Queue(out <- [] <- in)"


def test_str_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert str(queue) == "Queue(out <- [1, 2, 3] <- in)"


def test_bool_empty_queue() -> None:
    queue = Queue()
    assert not queue


def test_bool_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert queue


def test_enqueue_empty_queue() -> None:
    queue = Queue()
    queue.enqueue(1)
    assert list(queue) == [1]


def test_enqueue_non_empty_queue() -> None:
    queue = Queue([1])
    queue.enqueue(2)
    assert list(queue) == [1, 2]


def test_dequeue_empty_queue() -> None:
    queue = Queue()

    with pytest.raises(IndexError, match="dequeue from empty queue"):
        queue.dequeue()


def test_dequeue_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert queue.dequeue() == 1
    assert list(queue) == [2, 3]


def test_dequeue_multiple_values() -> None:
    queue = Queue([1, 2, 3])
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert list(queue) == []


def test_dequeue_last_element() -> None:
    queue = Queue([1])
    assert queue.dequeue() == 1
    assert list(queue) == []


def test_peek_empty_queue() -> None:
    queue = Queue()

    with pytest.raises(IndexError, match="peek from empty queue"):
        queue.peek()


def test_peek_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert queue.peek() == 1
    assert list(queue) == [1, 2, 3]


def test_peek_single_value_queue() -> None:
    queue = Queue([1])
    assert queue.peek() == 1
    assert list(queue) == [1]


def test_is_empty_empty_queue() -> None:
    queue = Queue()
    assert queue.is_empty()


def test_is_empty_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    assert not queue.is_empty()


def test_clear_empty_queue() -> None:
    queue = Queue()
    queue.clear()
    assert list(queue) == []


def test_clear_non_empty_queue() -> None:
    queue = Queue([1, 2, 3])
    queue.clear()
    assert list(queue) == []


def test_enqueue_after_emptying_queue() -> None:
    queue = Queue([1, 2, 3])
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    queue.enqueue(4)
    assert list(queue) == [4]


def test_enqueue_after_clear() -> None:
    queue = Queue([1, 2, 3])
    queue.clear()
    queue.enqueue(4)
    assert list(queue) == [4]
