import pytest

from dsa.data_structures.hash_set import HashSet


def test_build_empty_hash_set() -> None:
    hs = HashSet()
    assert len(hs) == 0


def test_build_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert len(hs) == 3
    assert "a" in hs
    assert "b" in hs
    assert "c" in hs


def test_build_non_empty_hash_set_repeated_elements() -> None:
    hs = HashSet(["a", "b", "c", "a", "b"])
    assert len(hs) == 3
    assert "a" in hs
    assert "b" in hs
    assert "c" in hs


def test_len_empty_hash_set() -> None:
    hs = HashSet()
    assert len(hs) == 0


def test_len_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert len(hs) == 3


def test_iter_empty_hash_set() -> None:
    hs = HashSet()
    assert len(hs) == 0


def test_iter_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert set(hs) == {"a", "b", "c"}


def test_repr_empty_hash_set() -> None:
    hs = HashSet()
    assert repr(hs) == "HashSet({})"


def test_repr_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert repr(hs) == "HashSet({'a', 'b', 'c'})"


def test_str_empty_hash_set() -> None:
    hs = HashSet()
    assert str(hs) == "HashSet({})"


def test_str_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert str(hs) == "HashSet({'a', 'b', 'c'})"


def test_bool_empty_hash_set() -> None:
    hs = HashSet()
    assert not hs


def test_bool_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert hs


def test_contains_empty_hash_set() -> None:
    hs = HashSet()
    assert "a" not in hs


def test_contains_existint_element() -> None:
    hs = HashSet(["a", "b", "c"])
    assert "a" in hs


def test_contains_non_existint_element() -> None:
    hs = HashSet(["a", "b", "c"])
    assert "d" not in hs


def test_add_empty_hash_set() -> None:
    hs = HashSet()
    hs.add("a")
    assert len(hs) == 1
    assert "a" in hs


def test_add_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    hs.add("d")
    assert len(hs) == 4
    assert "a" in hs
    assert "b" in hs
    assert "c" in hs
    assert "d" in hs


def test_add_existing_element() -> None:
    hs = HashSet(["a", "b", "c"])
    hs.add("a")
    assert len(hs) == 3
    assert "a" in hs
    assert "b" in hs
    assert "c" in hs


def test_remove_empty_hash_set() -> None:
    hs = HashSet()

    with pytest.raises(KeyError, match="a"):
        hs.remove("a")


def test_remove_existing_element() -> None:
    hs = HashSet(["a", "b", "c"])
    hs.remove("a")
    assert len(hs) == 2
    assert "b" in hs
    assert "c" in hs


def test_remove_non_existing_element() -> None:
    hs = HashSet(["a", "b", "c"])

    with pytest.raises(KeyError, match="d"):
        hs.remove("d")


def test_is_empty_empty_hash_set() -> None:
    hs = HashSet()
    assert hs.is_empty()


def test_is_empty_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    assert not hs.is_empty()


def test_clear_empty_hash_set() -> None:
    hs = HashSet()
    hs.clear()
    assert len(hs) == 0


def test_clear_non_empty_hash_set() -> None:
    hs = HashSet(["a", "b", "c"])
    hs.clear()
    assert len(hs) == 0
