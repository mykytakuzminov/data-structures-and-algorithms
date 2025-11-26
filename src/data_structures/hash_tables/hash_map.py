from typing import Any, Optional


class HashMap:
    """
    Hash Map implementation using chaining (buckets) for collision resolution.

    This data structure maps keys to values. It uses a list of buckets,
    where each bucket is a list of (key, value) tuples.

    Methods:
        put(key, value): Insert or update a key-value pair.
        get(key): Return the value for a key.
        remove(key): Remove a key-value pair.
        contains(key): Check if a key exists.
        is_empty(): Check if the map is empty.
        clear(): Remove all entries.
        keys(): Return a list of all keys.
        values(): Return a list of all values.
    """
    _capacity: int
    _length: int
    _buckets: list[list[tuple[Any, Any]]]

    def __init__(self, capacity: int = 8) -> None:
        """
        Initialize an empty hash map.

        Args:
            capacity: Initial number of buckets (default is 8).
        """
        self._capacity = capacity
        self._length = 0
        self._buckets = [[] for _ in range(capacity)]

    # --- Modification Methods ---

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair in the hash map.

        If the key already exists, its value is updated.
        If the key is new, it is added to the map.

        Args:
            key: Key to insert/update.
            value: Value associated with the key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        # Check if key exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key not found, append new pair
        bucket.append((key, value))
        self._length += 1

    def remove(self, key: Any) -> bool:
        """
        Remove a key-value pair by key.

        Args:
            key: Key to remove.

        Returns:
            True if key was removed, False if key was not found.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._length -= 1
                return True

        return False

    def clear(self) -> None:
        """
        Remove all key-value pairs from the hash map.
        """
        self._buckets = [[] for _ in range(self._capacity)]
        self._length = 0

    # --- Access & Search Methods ---

    def get(self, key: Any) -> Optional[Any]:
        """
        Return the value for the given key.

        Args:
            key: Key to retrieve.

        Returns:
            Value associated with the key, or None if key not found.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def contains(self, key: Any) -> bool:
        """
        Check if the hash map contains a specific key.

        Args:
            key: Key to search for.

        Returns:
            True if key exists, False otherwise.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def keys(self) -> list[Any]:
        """
        Return a list of all keys in the map.

        Returns:
            A list containing all keys.
        """
        all_keys = []
        for bucket in self._buckets:
            for k, _ in bucket:
                all_keys.append(k)
        return all_keys

    def values(self) -> list[Any]:
        """
        Return a list of all values in the map.

        Returns:
            A list containing all values.
        """
        all_values = []
        for bucket in self._buckets:
            for k, v in bucket:
                all_values.append(v)
        return all_values

    # --- Status & Internal Methods ---

    def is_empty(self) -> bool:
        """
        Check if the hash map is empty.

        Returns:
            True if the map is empty, False otherwise.
        """
        return self._length == 0

    def _hash(self, key: Any) -> int:
        """
        Compute the bucket index for a given key.

        Args:
            key: The key to compute hash for.

        Returns:
            Index in the internal bucket list.
        """
        return hash(key) % self._capacity

    # --- Magic Methods ---

    def __contains__(self, key: Any) -> bool:
        """Enable 'in' operator support (e.g., 'if key in map:')."""
        return self.contains(key)

    def __len__(self) -> int:
        """Return the total number of key-value pairs."""
        return self._length

    def __str__(self) -> str:
        """
        Return a string representation like a Python dictionary.

        Returns:
            String in format '{key1: value1, key2: value2}'
        """
        if self._length == 0:
            return "{}"

        pairs = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{repr(k)}: {repr(v)}")

        return "{" + ", ".join(pairs) + "}"
