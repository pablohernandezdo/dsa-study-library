import pytest

from dsa.data_structures.heap import Heap, MaxHeap, MinHeap


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_init_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls()
    assert list(heap) == []


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_init_non_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls([1, 2, 3])
    assert list(heap) == [1, 2, 3]


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_len_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls()
    assert len(heap) == 0


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_len_non_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls([1, 2, 3])
    assert len(heap) == 3


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_iter_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls()
    assert list(heap) == []


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_iter_non_empty_heap(heap_cls: type[Heap]) -> None:
    heap = heap_cls([1, 2, 3])
    assert list(heap) == [1, 2, 3]


@pytest.mark.parametrize(
    "heap_cls, values, expected_repr",
    [
        (MinHeap, [], "MinHeap([])"),
        (MinHeap, [1, 2, 3], "MinHeap([1, 2, 3])"),
        (MaxHeap, [], "MaxHeap([])"),
        (MaxHeap, [3, 2, 1], "MaxHeap([3, 2, 1])"),
    ],
)
def test_repr(heap_cls: type[Heap], values: list[int], expected_repr: str) -> None:
    heap = heap_cls(values)
    assert repr(heap) == expected_repr


@pytest.mark.parametrize(
    "heap_cls, values, expected_str",
    [
        (MinHeap, [], "MinHeap([])"),
        (MinHeap, [1, 2, 3], "MinHeap([1, 2, 3])"),
        (MaxHeap, [], "MaxHeap([])"),
        (MaxHeap, [3, 2, 1], "MaxHeap([3, 2, 1])"),
    ],
)
def test_str(heap_cls: type[Heap], values: list[int], expected_str: str) -> None:
    heap = heap_cls(values)
    assert str(heap) == expected_str


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_parent_index_calculation(heap_cls: type[Heap]) -> None:
    assert heap_cls.parent(1) == 0
    assert heap_cls.parent(2) == 0
    assert heap_cls.parent(3) == 1


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_left_child_index_calculation(heap_cls: type[Heap]) -> None:
    assert heap_cls.left_child(0) == 1
    assert heap_cls.left_child(1) == 3
    assert heap_cls.left_child(2) == 5


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_right_child_index_calculation(heap_cls: type[Heap]) -> None:
    assert heap_cls.right_child(0) == 2
    assert heap_cls.right_child(1) == 4
    assert heap_cls.right_child(2) == 6


@pytest.mark.parametrize(
    "heap_cls,values",
    [
        (MinHeap, [5, 4, 3, 2, 1]),
        (MinHeap, [9, 4, 7, 1, 0, 3]),
        (MinHeap, [10, 20, 15, 30, 40]),
        (MinHeap, [8, 6, 7, 5, 3, 0, 9]),
        (MaxHeap, [1, 2, 3, 4, 5]),
        (MaxHeap, [0, 1, 2, 3, 4, 5]),
        (MaxHeap, [40, 30, 20, 10, 5]),
        (MaxHeap, [3, 10, 5, 6, 2, 8, 1]),
    ],
)
def test_heapify(heap_cls: type[Heap], values: list[int]) -> None:
    heap = heap_cls.heapify(values)
    assert heap.is_heap()
    assert sorted(heap) == sorted(values)


@pytest.mark.parametrize(
    "heap_cls,values,expected_array",
    [
        (MinHeap, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        (MinHeap, [9, 4, 7, 1, 0, 3], [0, 1, 3, 4, 7, 9]),
        (MinHeap, [10, 20, 15, 30, 40], [10, 15, 20, 30, 40]),
        (MinHeap, [8, 6, 7, 5, 3, 0, 9], [0, 3, 5, 6, 7, 8, 9]),
        (MinHeap, [5, 1, 5, 3, 1], [1, 1, 3, 5, 5]),
        (MaxHeap, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (MaxHeap, [0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]),
        (MaxHeap, [40, 30, 20, 10, 5], [40, 30, 20, 10, 5]),
        (MaxHeap, [3, 10, 5, 6, 2, 8, 1], [10, 8, 6, 5, 3, 2, 1]),
        (MaxHeap, [5, 1, 5, 3, 1], [5, 5, 3, 1, 1]),
    ],
)
def test_heapsort(
    heap_cls: type[Heap], values: list[int], expected_array: list[int]
) -> None:
    sorted_array = heap_cls.heapsort(values)
    assert list(sorted_array) == expected_array


@pytest.mark.parametrize("heap_cls", [MinHeap, MaxHeap])
def test_peek_empty_heap_raises(heap_cls: type[Heap]) -> None:
    heap = heap_cls()
    with pytest.raises(IndexError, match="peek from empty heap"):
        heap.peek()


@pytest.mark.parametrize(
    "heap_cls,values,expected_value",
    [
        (MinHeap, [1, 2, 3], 1),
        (MaxHeap, [1, 2, 3], 3),
    ],
)
def test_peek(heap_cls: type[Heap], values: list[int], expected_value: int) -> None:
    heap = heap_cls.heapify(values)
    assert heap.peek() == expected_value


@pytest.mark.parametrize(
    "heap_cls, values, inserted, expected",
    [
        (MinHeap, [], 5, [5]),
        (MaxHeap, [], 5, [5]),
        (MinHeap, [1, 3, 5], 2, [1, 2, 5, 3]),
        (MaxHeap, [5, 3, 1], 4, [5, 4, 1, 3]),
    ],
)
def test_insert(
    heap_cls: type[Heap], values: list[int], inserted: int, expected: list[int]
) -> None:
    heap = heap_cls(values)
    heap.insert(inserted)
    assert list(heap) == expected
    assert heap.is_heap()


@pytest.mark.parametrize(
    "heap_cls, extract_method",
    [
        (MinHeap, "extract_min"),
        (MaxHeap, "extract_max"),
    ],
)
def test_extract_empty_heap_raises(heap_cls: type[Heap], extract_method: str) -> None:
    heap = heap_cls()

    with pytest.raises(IndexError, match="extract from empty heap"):
        getattr(heap, extract_method)()


@pytest.mark.parametrize(
    "heap_cls, values, method_name",
    [
        (MinHeap, [1], "extract_min"),
        (MaxHeap, [1], "extract_max"),
    ],
)
def test_extract_single_element(
    heap_cls: type[Heap], values: list[int], method_name: str
) -> None:
    heap = heap_cls.heapify(values)
    extracted = getattr(heap, method_name)()

    assert extracted == 1
    assert len(heap) == 0


@pytest.mark.parametrize(
    "heap_cls, values, method_name, expected",
    [
        (MinHeap, [3, 1, 4, 2], "extract_min", [1, 2, 3, 4]),
        (MaxHeap, [3, 1, 4, 2], "extract_max", [4, 3, 2, 1]),
    ],
)
def test_extract_order(
    heap_cls: type[Heap], values: list[int], method_name: str, expected: list[int]
) -> None:
    heap = heap_cls.heapify(values)
    extracted = [getattr(heap, method_name)() for _ in range(len(heap))]
    assert extracted == expected
    assert list(heap) == []


@pytest.mark.parametrize(
    "heap_cls, values, expected_value",
    [
        (MinHeap, [], True),
        (MinHeap, [1, 3, 5, 7, 9], True),
        (MinHeap, [1, 9, 5, 7, 3], False),
        (MinHeap, [5, 5, 5, 5, 5], True),
        (MaxHeap, [], True),
        (MaxHeap, [9, 7, 5, 3, 1], True),
        (MaxHeap, [9, 1, 5, 3, 7], False),
        (MaxHeap, [5, 5, 5, 5, 5], True),
    ],
)
def test_is_heap(heap_cls: type[Heap], values: list[int], expected_value: bool) -> None:
    heap = heap_cls(values)
    assert heap.is_heap() == expected_value
