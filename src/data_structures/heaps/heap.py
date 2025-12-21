from typing import Any


class Heap:
    """
    Min-Heap implementation using a dynamic array.

    A Min-Heap is a complete binary tree where the value of each node
    is less than or equal to the values of its children, ensuring
    the smallest element is always at the root.

    Methods:
        heapify(arr): Transform a list into a heap.
        push(data): Insert a new element into the heap.
        pop(): Remove and return the smallest element (root).
        sort(): Return all elements in ascending order without destroying the heap.
        peek(): Get the smallest value without removing it.
        is_empty(): Check if the heap contains no elements.
        clear(): Remove all elements.
    """
    _arr: list[Any]

    def __init__(self) -> None:
        """Initialize an empty heap."""
        self._arr = []

    def _is_better(self, val1: Any, val2: Any) -> bool:
        """
        Comparison strategy to determine the priority of elements.

        Args:
            val1: First value to compare.
            val2: Second value to compare.

        Returns:
            True if val1 has higher priority than val2.
        """
        raise NotImplementedError("Subclasses must implement _is_better")

    # --- Modification Methods ---

    def heapify(self, arr: list[Any]) -> None:
        """
        Transform a list into a valid Min-Heap.

        Args:
            arr: A list of elements to be transformed.
        """
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)
        self._arr = list(arr)

    def push(self, data: Any) -> None:
        """
        Add a new element to the heap while maintaining heap property.

        Args:
            data: The element to be added.
        """
        self._arr.append(data)
        self._sift_up(self._arr, len(self._arr) - 1)

    def pop(self) -> Any:
        """
        Remove and return the smallest element from the heap.

        Returns:
            The smallest value (root of the heap).

        Raises:
            IndexError: If the heap is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty heap")

        root_data = self._arr[0]
        last_element = self._arr.pop()

        if not self.is_empty():
            self._arr[0] = last_element
            self._sift_down(self._arr, len(self._arr), 0)

        return root_data

    # --- Access & Utility Methods ---

    def sort(self) -> list[Any]:
        """
        Return all elements in sorted order.

        This method performs Heapsort but preserves the internal state
        of the heap by using a backup of the original data.

        Returns:
            A list of all elements in ascending order.
        """
        original_arr = self._arr[:]
        result = []

        try:
            while not self.is_empty():
                result.append(self.pop())
        finally:
            self._arr = original_arr

        return result

    def peek(self) -> Any:
        """
        Return the smallest element without removing it.

        Returns:
            The root value of the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self.is_empty():
            raise IndexError("peek from an empty heap")
        return self._arr[0]

    def is_empty(self) -> bool:
        """
        Check if the heap contains no elements.

        Returns:
            True if the heap is empty, False otherwise.
        """
        return len(self._arr) == 0

    def clear(self) -> None:
        """
        Remove all elements from the heap.
        """
        self._arr = []

    # --- Internal Utility Methods ---

    def _sift_down(self, arr: list[Any], n: int, i: int) -> None:
        """
        Move an element down the tree to its correct position (Heapify-down).

        Args:
            arr: The list representing the heap.
            n: Number of elements in the heap.
            i: Index of the element to sift down.
        """
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self._is_better(arr[left], arr[smallest]):
            smallest = left

        if right < n and self._is_better(arr[right], arr[smallest]):
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self._sift_down(arr, n, smallest)

    def _sift_up(self, arr: list[Any], i: int) -> None:
        """
        Move an element up the tree to its correct position (Bubble-up).

        Args:
            arr: The list representing the heap.
            i: Index of the element to sift up.
        """
        if i == 0:
            return

        parent = (i - 1) // 2
        if self._is_better(arr[i], arr[parent]):
            arr[i], arr[parent] = arr[parent], arr[i]
            self._sift_up(arr, parent)

    # --- Standard Python Methods ---

    def __len__(self) -> int:
        """
        Get the number of elements in the heap.

        Returns:
            The count of elements.
        """
        return len(self._arr)
