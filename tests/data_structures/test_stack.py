import pytest

from dsa.data_structures.stack import Stack


def test_build_empty_stack() -> None:
    stack = Stack()
    assert list(stack) == []


def test_build_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert list(stack) == [3, 2, 1]


def test_len_empty_stack() -> None:
    stack = Stack()
    assert len(stack) == 0


def test_len_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert len(stack) == 3


def test_repr_empty_stack() -> None:
    stack = Stack()
    assert repr(stack) == "Stack([] <- top)"


def test_repr_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert repr(stack) == "Stack([1, 2, 3] <- top)"


def test_str_empty_stack() -> None:
    stack = Stack()
    assert str(stack) == "Stack([] <- top)"


def test_str_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert str(stack) == "Stack([1, 2, 3] <- top)"


def test_bool_empty_stack() -> None:
    stack = Stack()
    assert not stack


def test_bool_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert stack


def test_iter_empty_stack() -> None:
    stack = Stack()
    assert list(stack) == []


def test_iter_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert list(stack) == [3, 2, 1]


def test_iter_is_repeatable() -> None:
    stack = Stack([1, 2, 3])
    assert list(stack) == [3, 2, 1]
    assert list(stack) == [3, 2, 1]


def test_reversed_empty_stack() -> None:
    stack = Stack()
    assert list(stack) == []


def test_reversed_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert list(reversed(stack)) == [1, 2, 3]


def test_reversed_is_repeatable() -> None:
    stack = Stack([1, 2, 3])
    assert list(reversed(stack)) == [1, 2, 3]
    assert list(reversed(stack)) == [1, 2, 3]


def test_push_empty_stack() -> None:
    stack = Stack()
    stack.push(1)
    assert list(stack) == [1]


def test_push_non_empty_stack() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert list(stack) == [2, 1]


def test_pop_empty_stack() -> None:
    stack = Stack()

    with pytest.raises(IndexError, match="pop from empty stack"):
        stack.pop()


def test_pop_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    value = stack.pop()
    assert value == 3
    assert list(stack) == [2, 1]


def test_peek_empty_stack() -> None:
    stack = Stack()

    with pytest.raises(IndexError, match="peek from empty stack"):
        _ = stack.peek()


def test_peek_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    value = stack.peek()
    assert value == 3
    assert list(stack) == [3, 2, 1]


def test_is_empty_empty_stack() -> None:
    stack = Stack()
    assert stack.is_empty()


def test_is_empty_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    assert not stack.is_empty()


def test_clear_empty_stack() -> None:
    stack = Stack()
    stack.clear()
    assert list(stack) == []


def test_clear_non_empty_stack() -> None:
    stack = Stack([1, 2, 3])
    stack.clear()
    assert list(stack) == []


def test_clear_then_push() -> None:
    stack = Stack([1, 2, 3])
    stack.clear()
    stack.push(4)
    assert list(stack) == [4]


def test_lifo_behavior() -> None:
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
