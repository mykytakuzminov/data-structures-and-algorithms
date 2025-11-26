from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    """Protocol for objects that support comparison operations."""
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def binary_search(arr: list[T], val: T) -> bool:
    """
    Performs a binary search on a sorted list.

    Args:
        arr: Sorted list of comparable elements (int, str, etc.).
        val: Value to find.

    Returns:
        True if found, False otherwise.
    """
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        m = left + ((right - left) // 2)

        if val == arr[m]:
            return True
        elif val < arr[m]:
            right = m - 1
        elif val > arr[m]:
            left = m + 1

    return False
