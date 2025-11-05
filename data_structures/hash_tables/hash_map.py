class HashMap:
    """
    Hash map with basic operations.

    Methods:
        is_empty(): Check if the hash map is empty.
        put(key, value): Insert or update a key-value pair.
        get(key): Get the value for a key.
        remove(key): Remove a key-value pair.
    """
    def __init__(self, capacity=8):
        """Initialize an empty hash map with given capacity."""
        self._capacity = capacity
        self._length = 0
        self._buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        """Compute index for a given key."""
        return hash(key) % self._capacity

    def is_empty(self):
        """Return True if the hash map is empty, else False."""
        return self._length == 0

    def put(self, key, value):
        """Insert or update a key-value pair in the hash map.

        Args:
            key: Key to insert/update.
            value: Value associated with the key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._length += 1

    def get(self, key):
        """Return the value for the given key, or None if key not found.

        Args:
            key: Key to retrieve.

        Returns:
            Value associated with the key or None.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        """Remove a key-value pair by key.

        Args:
            key: Key to remove.

        Returns:
            True if key was removed, False otherwise.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._length -= 1
                return True

        return False

    def __len__(self):
        """Return the total number of key-value pairs."""
        return self._length

    def __str__(self):
        """Return a string representation like a Python dictionary."""
        if self._length == 0:
            return "{}"

        pairs = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{repr(k)}: {repr(v)}")

        return "{" + ", ".join(pairs) + "}"
