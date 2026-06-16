import pytest

from dsa.data_structures.deque import Deque


def test_build_empty_deque() -> None:
    deque = Deque()
    assert list(deque) == []


def test_build_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert list(deque) == [1, 2, 3]


def test_len_empty_deque() -> None:
    deque = Deque()
    assert len(deque) == 0


def test_len_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert len(deque) == 3


def test_iter_empty_queue() -> None:
    deque = Deque()
    assert list(deque) == []


def test_iter_non_empty_queue() -> None:
    deque = Deque([1, 2, 3])
    assert list(deque) == [1, 2, 3]


def test_iter_is_repeatable() -> None:
    deque = Deque([1, 2, 3])
    assert list(deque) == [1, 2, 3]
    assert list(deque) == [1, 2, 3]


def test_reversed_empty_queue() -> None:
    deque = Deque()
    assert list(reversed(deque)) == []


def test_reversed_non_empty_queue() -> None:
    deque = Deque([1, 2, 3])
    assert list(reversed(deque)) == [3, 2, 1]


def test_repr_empty_queue() -> None:
    deque = Deque()
    assert repr(deque) == "Deque(left -> [] <- right)"


def test_repr_non_empty_queue() -> None:
    deque = Deque([1, 2, 3])
    assert repr(deque) == "Deque(left -> [1, 2, 3] <- right)"


def test_str_empty_queue() -> None:
    deque = Deque()
    assert repr(deque) == "Deque(left -> [] <- right)"


def test_str_non_empty_queue() -> None:
    deque = Deque([1, 2, 3])
    assert repr(deque) == "Deque(left -> [1, 2, 3] <- right)"


def test_bool_empty_queue() -> None:
    deque = Deque()
    assert not deque


def test_bool_non_empty_queue() -> None:
    deque = Deque([1, 2, 3])
    assert deque


def test_append_left_empty_deque() -> None:
    deque = Deque()
    deque.append_left(1)
    assert list(deque) == [1]


def test_append_left_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    deque.append_left(4)
    assert list(deque) == [4, 1, 2, 3]


def test_append_right_empty_deque() -> None:
    deque = Deque()
    deque.append_right(1)
    assert list(deque) == [1]


def test_append_right_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    deque.append_right(4)
    assert list(deque) == [1, 2, 3, 4]


def test_pop_left_empty_deque() -> None:
    deque = Deque()

    with pytest.raises(IndexError, match="pop left from empty deque"):
        deque.pop_left()


def test_pop_left_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert deque.pop_left() == 1
    assert list(deque) == [2, 3]


def test_pop_right_empty_deque() -> None:
    deque = Deque()

    with pytest.raises(IndexError, match="pop right from empty deque"):
        deque.pop_right()


def test_pop_right_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert deque.pop_right() == 3
    assert list(deque) == [1, 2]


def test_peek_left_empty_deque() -> None:
    deque = Deque()

    with pytest.raises(IndexError, match="peek left from empty deque"):
        deque.peek_left()


def test_peek_left_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert deque.peek_left() == 1
    assert list(deque) == [1, 2, 3]


def test_peek_right_empty_deque() -> None:
    deque = Deque()

    with pytest.raises(IndexError, match="peek right from empty deque"):
        deque.peek_right()


def test_peek_right_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert deque.peek_right() == 3
    assert list(deque) == [1, 2, 3]


def test_is_empty_empty_deque() -> None:
    deque = Deque()
    assert deque.is_empty()


def test_is_empty_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    assert not deque.is_empty()


def test_clear_empty_deque() -> None:
    deque = Deque()
    deque.clear()
    assert list(deque) == []


def test_clear_non_empty_deque() -> None:
    deque = Deque([1, 2, 3])
    deque.clear()
    assert list(deque) == []


def test_pop_left_last_element() -> None:
    deque = Deque([1])
    assert deque.pop_left() == 1
    assert list(deque) == []


def test_pop_right_last_element() -> None:
    deque = Deque([1])
    assert deque.pop_right() == 1
    assert list(deque) == []


def test_append_left_after_clear() -> None:
    deque = Deque([1, 2, 3])
    deque.clear()
    deque.append_right(1)
    assert list(deque) == [1]


def test_append_right_after_clear() -> None:
    deque = Deque([1, 2, 3])
    deque.clear()
    deque.append_right(4)
    assert list(deque) == [4]


def test_append_left_after_dequeing_all() -> None:
    deque = Deque([1, 2, 3])

    assert deque.pop_left() == 1
    assert deque.pop_left() == 2
    assert deque.pop_left() == 3

    deque.append_left(4)
    assert list(deque) == [4]


def test_append_right_after_dequeing_all() -> None:
    deque = Deque([1, 2, 3])

    assert deque.pop_left() == 1
    assert deque.pop_left() == 2
    assert deque.pop_left() == 3

    deque.append_right(4)
    assert list(deque) == [4]
