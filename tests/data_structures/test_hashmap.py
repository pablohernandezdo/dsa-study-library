import pytest

from dsa.data_structures.chaining_hash_map import HashMap


def test_build_empty_hashmap() -> None:
    hm = HashMap()
    assert len(hm) == 0
    assert list(hm) == []


def test_build_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert len(hm) == 3
    assert hm["a"] == 1
    assert hm["b"] == 2
    assert hm["c"] == 3


def test_build_invalid_capacity_hashmap() -> None:
    with pytest.raises(ValueError, match="capacity must be positive"):
        HashMap(capacity=0)


def test_len_empty_hashmap() -> None:
    hm = HashMap()
    assert len(hm) == 0


def test_len_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert len(hm) == 3


def test_iter_empty_hashmap() -> None:
    hm = HashMap()
    assert set(hm) == set()


def test_iter_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    keys = list(hm)
    assert len(keys) == 3
    assert set(keys) == {"a", "b", "c"}


def test_repr_empty_hashmap() -> None:
    hm = HashMap()
    assert repr(hm) == "HashMap({})"


def test_repr_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert repr(hm) == "HashMap({'a': 1, 'b': 2, 'c': 3})"


def test_str_empty_hashmap() -> None:
    hm = HashMap()
    assert str(hm) == "HashMap({})"


def test_str_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert str(hm) == "HashMap({'a': 1, 'b': 2, 'c': 3})"


def test_bool_empty_hashmap() -> None:
    hm = HashMap()
    assert not hm


def test_bool_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert hm


def test_contains_dunder_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert "a" in hm


def test_contains_dunder_missing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert "d" not in hm


def test_setitem_empty_hashmap() -> None:
    hm = HashMap()
    hm["a"] = 1
    assert hm["a"] == 1


def test_setitem_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    hm["d"] = 4
    assert hm["d"] == 4


def test_setitem_updates_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    hm["a"] = 4
    assert hm["a"] == 4


def test_getitem_empty_hashmap() -> None:
    hm = HashMap()
    with pytest.raises(KeyError, match="a"):
        hm["a"]


def test_getitem_missing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    with pytest.raises(KeyError, match="d"):
        hm["d"]


def test_getitem_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert hm["a"] == 1


def test_delitem_empty_hashmap() -> None:
    hm = HashMap()
    with pytest.raises(KeyError, match="a"):
        del hm["a"]


def test_delitem_missing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    with pytest.raises(KeyError, match="d"):
        del hm["d"]


def test_delitem_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    del hm["a"]
    assert len(hm) == 2
    assert set(hm) == {"b", "c"}


def test_put_empty_hashmap() -> None:
    hm = HashMap()
    hm.put("a", 1)
    assert len(hm) == 1
    assert hm["a"] == 1


def test_put_non_empty_hashmap() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    hm.put("d", 4)
    assert len(hm) == 4
    assert hm["a"] == 1
    assert hm["b"] == 2
    assert hm["c"] == 3
    assert hm["d"] == 4


def test_put_duplicate_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    hm.put("a", 4)
    assert len(hm) == 3
    assert hm["a"] == 4
    assert hm["b"] == 2
    assert hm["c"] == 3


def test_get_empty_hashmap() -> None:
    hm = HashMap()
    with pytest.raises(KeyError, match="a"):
        hm.get("a")


def test_get_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert hm.get("a") == 1


def test_remove_empty_hashmap() -> None:
    hm = HashMap()
    with pytest.raises(KeyError, match="a"):
        hm.remove("a")


def test_remove_missing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    with pytest.raises(KeyError, match="d"):
        hm.remove("d")


def test_remove_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    hm.remove("a")
    assert len(hm) == 2
    assert hm["b"] == 2
    assert hm["c"] == 3


def test_contains_empty_hashmap() -> None:
    hm = HashMap()
    assert not hm.contains("a")


def test_contains_missing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert not hm.contains("d")


def test_contains_existing_key() -> None:
    hm = HashMap([("a", 1), ("b", 2), ("c", 3)])
    assert hm.contains("a")


def test_resize_preserve_existing_values() -> None:
    hm = HashMap(capacity=2)

    hm["a"] = 1
    hm["b"] = 2  # triggers resize

    assert hm["a"] == 1
    assert hm["b"] == 2


def test_resize_doubles_capacity() -> None:
    hm = HashMap(capacity=2)

    hm["a"] = 1
    hm["b"] = 2  # triggers resize

    assert hm._size == 2  # type:ignore
    assert hm._capacity == 4  # type:ignore


def test_resize_maintains_size() -> None:
    hm = HashMap(capacity=2)

    hm["a"] = 1
    hm["b"] = 2  # triggers resize

    assert hm._size == 2  # type:ignore


def test_collision_put() -> None:
    hm = HashMap()
    hm._hash = lambda _: 0  # type:ignore

    hm.put("a", 1)
    hm.put("b", 2)

    assert hm["a"] == 1
    assert hm["b"] == 2


def test_collision_update() -> None:
    hm = HashMap()
    hm._hash = lambda _: 0  # type:ignore

    hm.put("a", 1)
    hm.put("b", 2)
    hm.put("a", 3)

    assert hm["a"] == 3
    assert hm["b"] == 2


def test_collision_remove() -> None:
    hm = HashMap()
    hm._hash = lambda _: 0  # type:ignore

    hm.put("a", 1)
    hm.put("b", 2)
    del hm["a"]

    assert len(hm) == 1
    assert hm["b"] == 2
