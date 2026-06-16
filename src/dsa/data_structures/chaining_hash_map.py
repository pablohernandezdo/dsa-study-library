from collections.abc import Iterator


class HashMap:
    """
    Hash Map implementation that uses buckets to store key-value pairs. Buckets
    are implemented as Python's lists that store tuples of key-value pairs
    and collisions are handled using chaining. The Hash Map is resized whenever
    its load factor surpasses LOAD_FACTOR_THRESHOLD, in which case a new set of
    buckets with double capacity is created and every element is rehashed.

    Operations:
        - put: average O(1) amortized, worst O(n)
        - get: average O(1), worst O(n)
        - remove: average O(1), worst O(n)
        - contains: average O(1), worst O(n)

    """

    LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(
        self,
        kv_pairs: list[tuple[str, int]] | None = None,
        capacity: int = 8,
    ) -> None:
        """
        Build a Hash Map from a list of key-value pairs.

        If no key-value pairs are provided, an empty hash map is created.

        Args:
            kv_pairs: list of key-value pairs to populate the hash map.

            capacity: number of buckets to store key-value pairs. Eight by default.

        Raises:
            ValueError: if the capacity provided is less than or equal to zero.
        """

        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self._size = 0
        self._capacity = capacity
        self._buckets: list[list[tuple[str, int]]] = [[] for _ in range(self._capacity)]

        if kv_pairs:
            for k, v in kv_pairs:
                self.put(k, v)

    def __len__(self) -> int:
        """
        Return the number of key-value pairs in the hash map.

        Time Complexity:
            - O(1)
        """

        return self._size

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over the keys in the hash map.

        Time Complexity:
            - O(n)
        """

        for bucket in self._buckets:
            for key, _ in bucket:
                yield key

    def __repr__(self) -> str:
        """
        Time Complexity:
            - O(n log n)
        """

        items = sorted(
            (f"{key!r}: {value!r}" for bucket in self._buckets for key, value in bucket)
        )
        return f"HashMap({{{', '.join(items)}}})"

    def __str__(self) -> str:
        return repr(self)

    def __bool__(self) -> bool:
        """
        Time Complexity:
                O(1)
        """

        return bool(self._size)

    def __contains__(self, key: str) -> bool:
        """
        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        return self.contains(key)

    def __setitem__(self, key: str, value: int) -> None:
        """
        Time Complexity:
            - Average: O(1) amortized
            - Worst: O(n)
        """

        self.put(key, value)

    def __getitem__(self, key: str) -> int:
        """
        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        return self.get(key)

    def __delitem__(self, key: str) -> None:
        """
        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        self.remove(key)

    def _hash(self, key: str) -> int:
        """
        Hash function used to map keys to buckets.

        Time Complexity:
            - O(1)
        """

        return hash(key) % self._capacity

    @property
    def load_factor(self) -> float:
        """
        Time Complexity:
            - O(1)
        """

        return self._size / self._capacity

    def _resize(self) -> None:
        """
        Duplicate the capacity of the hash map and re-hash all existing elements.

        Time Complexity:
            - O(n)
        """

        old_buckets = self._buckets

        self._size = 0
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]

        # re hash and re store
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key: str, value: int) -> None:
        """
        Add a key value pair to the hash map, or update the value of the key
        if it exists.

        If after adding the key-value pair the load factor of the hash map surpasses
        the threshold given by LOAD_FACTOR_THRESHOLD, resize the hash map.

        Time Complexity:
            - Average: O(1) amortized
            - Worst: O(n)
        """

        bucket_idx = self._hash(key)
        bucket = self._buckets[bucket_idx]

        # update
        for idx, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[idx] = (key, value)
                return

        # store new
        bucket.append((key, value))
        self._size += 1

        if self.load_factor > self.LOAD_FACTOR_THRESHOLD:
            self._resize()

    def get(self, key: str) -> int:
        """
        Return the value for a key.

        Args:
            key: the key whose value is returned.

        Raises:
            KeyError: if the key is not present in the hash map.

        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        bucket_idx = self._hash(key)
        bucket = self._buckets[bucket_idx]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        raise KeyError(key)

    def remove(self, key: str) -> None:
        """
        Remove a key-value pair for a specific key.

        Args:
            key: the key to remove from the hash map.

        Raises:
            KeyError: if the key is not present in the hash map.

        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        bucket_idx = self._hash(key)
        bucket = self._buckets[bucket_idx]

        for idx, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[idx]
                self._size -= 1
                return

        raise KeyError(key)

    def contains(self, key: str) -> bool:
        """
        Return whether a specific key is present or not in the hash map.

        Args:
            key: the key to look for in the hash map.

        Time Complexity:
            - Average: O(1)
            - Worst: O(n)
        """

        bucket_idx = self._hash(key)
        bucket = self._buckets[bucket_idx]

        for stored_key, _ in bucket:
            if stored_key == key:
                return True

        return False
