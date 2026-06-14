import pytest

from dsa.data_structures.doubly_linked_list import DoublyLinkedList


def test_create_empty_doubly_linked_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert list(dlinked_list) == []


def test_create_non_empty_doubly_linked_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert list(dlinked_list) == [1, 2, 3]


def test_head_and_tail_after_empty_construction() -> None:
    dlinked_list = DoublyLinkedList()
    assert dlinked_list.head is None
    assert dlinked_list.tail is None


def test_head_and_tail_after_construction() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert dlinked_list.head is not None
    assert dlinked_list.tail is not None
    assert dlinked_list.head.value == 1
    assert dlinked_list.tail.value == 3


def test_len_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert len(dlinked_list) == 0


def test_len_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert len(dlinked_list) == 3


def test_iter_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert list(dlinked_list) == []


def test_iter_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert list(dlinked_list) == [1, 2, 3]


def test_iter_is_repeatable() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert list(dlinked_list) == [1, 2, 3]
    assert list(dlinked_list) == [1, 2, 3]


def test_repr_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert dlinked_list.__repr__() == "DoublyLinkedList([])"


def test_repr_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert dlinked_list.__repr__() == "DoublyLinkedList([1, 2, 3])"


def test_str_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert str(dlinked_list) == ""


def test_str_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert str(dlinked_list) == "1 <-> 2 <-> 3"


def test_reversed_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    assert list(reversed(dlinked_list)) == []


def test_reversed_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert list(reversed(dlinked_list)) == [3, 2, 1]


def test_insert_front_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    dlinked_list.insert_front(1)
    assert list(dlinked_list) == [1]


def test_insert_front_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([2, 3, 4])
    dlinked_list.insert_front(1)
    assert list(dlinked_list) == [1, 2, 3, 4]


def test_insert_front_updates_head() -> None:
    dlinked_list = DoublyLinkedList([2, 3])
    dlinked_list.insert_front(1)
    assert dlinked_list.head is not None
    assert dlinked_list.head.value == 1


def test_insert_back_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    dlinked_list.insert_back(1)
    assert list(dlinked_list) == [1]


def test_insert_front_updates_tail() -> None:
    dlinked_list = DoublyLinkedList([1, 2])
    dlinked_list.insert_back(3)
    assert dlinked_list.tail is not None
    assert dlinked_list.tail.value == 3


def test_insert_back_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.insert_back(4)
    assert list(dlinked_list) == [1, 2, 3, 4]


def test_insert_front_back_front_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    dlinked_list.insert_front(1)
    dlinked_list.insert_back(2)
    dlinked_list.insert_front(3)
    assert list(dlinked_list) == [3, 1, 2]


def test_insert_front_back_front_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([3, 4, 5])
    dlinked_list.insert_front(2)
    dlinked_list.insert_back(6)
    dlinked_list.insert_front(1)
    assert list(dlinked_list) == [1, 2, 3, 4, 5, 6]


def test_insert_back_front_back_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([2, 3, 4])
    dlinked_list.insert_back(5)
    dlinked_list.insert_front(1)
    dlinked_list.insert_back(6)
    assert list(dlinked_list) == [1, 2, 3, 4, 5, 6]


def test_find_empty_list() -> None:
    dlinked_list = DoublyLinkedList()

    with pytest.raises(ValueError, match="1 not found in list"):
        dlinked_list.find(1)


def test_find_existing_element() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    assert dlinked_list.find(2) == 1


def test_find_non_existing_element() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])

    with pytest.raises(ValueError, match="4 not found in list"):
        dlinked_list.find(4)


def test_delete_from_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    dlinked_list.delete(1)
    assert list(dlinked_list) == []


def test_delete_existing_value() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.delete(1)
    assert list(dlinked_list) == [2, 3]


def test_delete_existing_value_single_element_list() -> None:
    dlinked_list = DoublyLinkedList([1])
    dlinked_list.delete(1)
    assert list(dlinked_list) == []


def test_delete_non_existing_value() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.delete(4)
    assert list(dlinked_list) == [1, 2, 3]


def test_delete_first_occurrence() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 2, 3])
    dlinked_list.delete(2)
    assert list(dlinked_list) == [1, 2, 3]


def test_delete_head() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.delete(1)
    assert list(dlinked_list) == [2, 3]


def test_delete_middle() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.delete(2)
    assert list(dlinked_list) == [1, 3]


def test_delete_tail() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.delete(3)
    assert list(dlinked_list) == [1, 2]


def test_clear_empty_list() -> None:
    dlinked_list = DoublyLinkedList()
    dlinked_list.clear()
    assert list(dlinked_list) == []


def test_clear_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    dlinked_list.clear()
    assert list(dlinked_list) == []


def test_pop_back_empty_list() -> None:
    dlinked_list = DoublyLinkedList()

    with pytest.raises(IndexError, match="pop from empty list"):
        dlinked_list.pop_back()


def test_pop_back_single_element_list() -> None:
    dlinked_list = DoublyLinkedList([1])
    value = dlinked_list.pop_back()

    assert value == 1
    assert list(dlinked_list) == []


def test_pop_back_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    value = dlinked_list.pop_back()

    assert value == 3
    assert list(dlinked_list) == [1, 2]


def test_pop_front_empty_list() -> None:
    dlinked_list = DoublyLinkedList()

    with pytest.raises(IndexError, match="pop from empty list"):
        dlinked_list.pop_front()


def test_pop_front_single_element_list() -> None:
    dlinked_list = DoublyLinkedList([1])
    value = dlinked_list.pop_front()

    assert value == 1
    assert list(dlinked_list) == []


def test_pop_front_non_empty_list() -> None:
    dlinked_list = DoublyLinkedList([1, 2, 3])
    value = dlinked_list.pop_front()

    assert value == 1
    assert list(dlinked_list) == [2, 3]
