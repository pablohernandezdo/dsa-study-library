import pytest

from dsa.data_structures.linked_list import LinkedList


def test_create_empty_linked_list() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []


def test_create_non_empty_linked_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert list(linked_list) == [1, 2, 3]


def test_len_empty_list() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0


def test_len_non_empty_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert len(linked_list) == 3


def test_iter_empty_list() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []


def test_iter_non_empty_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert list(linked_list) == [1, 2, 3]


def test_iter_is_repeatable() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert list(linked_list) == [1, 2, 3]
    assert list(linked_list) == [1, 2, 3]


def test_repr_empty_linked_list() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == "LinkedList([])"


def test_repr_one_item_linked_list() -> None:
    linked_list = LinkedList([10])
    assert linked_list.__repr__() == "LinkedList([10])"


def test_repr_non_empty_linked_list() -> None:
    linked_list = LinkedList([30, 20, 10])
    assert linked_list.__repr__() == "LinkedList([30, 20, 10])"


def test_str_empty_linked_list() -> None:
    linked_list = LinkedList()
    assert str(linked_list) == ""


def test_str_one_item_linked_list() -> None:
    linked_list = LinkedList([10])
    assert str(linked_list) == "10"


def test_str_non_empty_linked_list() -> None:
    linked_list = LinkedList([30, 20, 10])
    assert str(linked_list) == "30 -> 20 -> 10"


def test_insert_front_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.insert_front(10)
    assert list(linked_list) == [10]


def test_insert_front_non_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.insert_front(10)
    linked_list.insert_front(20)
    assert list(linked_list) == [20, 10]


def test_insert_back_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.insert_back(10)
    assert list(linked_list) == [10]


def test_insert_back_non_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.insert_back(10)
    linked_list.insert_back(20)
    assert list(linked_list) == [10, 20]


def test_find_empty_linked_list() -> None:
    linked_list = LinkedList()

    with pytest.raises(ValueError, match="10 is not in list"):
        linked_list.find(10)


def test_find_first_value_linked_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.find(1) == 0


def test_find_middle_value_linked_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.find(2) == 1


def test_find_last_value_linked_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.find(3) == 2


def test_find_missing_value_linked_list() -> None:
    linked_list = LinkedList([1, 2, 3])

    with pytest.raises(ValueError, match="10 is not in list"):
        linked_list.find(10)


def test_delete_from_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.delete(10)
    assert list(linked_list) == []


def test_delete_head_node() -> None:
    linked_list = LinkedList([10, 20, 30])
    linked_list.delete(10)
    assert list(linked_list) == [20, 30]


def test_delete_middle_node() -> None:
    linked_list = LinkedList([10, 20, 30])
    linked_list.delete(20)
    assert list(linked_list) == [10, 30]


def test_delete_tail_node() -> None:
    linked_list = LinkedList([10, 20, 30])
    linked_list.delete(30)
    assert list(linked_list) == [10, 20]


def test_delete_value_not_in_list() -> None:
    linked_list = LinkedList([10, 20, 30])
    linked_list.delete(40)
    assert list(linked_list) == [10, 20, 30]


def test_delete_only_first_occurrence() -> None:
    linked_list = LinkedList([10, 20, 10, 30])
    linked_list.delete(10)
    assert list(linked_list) == [20, 10, 30]


def test_clear_empty_list() -> None:
    linked_list = LinkedList()
    linked_list.clear()
    assert list(linked_list) == []


def test_clear_non_empty_list() -> None:
    linked_list = LinkedList([1, 2, 3])
    linked_list.clear()
    assert list(linked_list) == []
