from typing import TypeVar, Protocol


class Comparable(Protocol):
    def __lt__(self, other: "Comparable", /) -> bool: ...
    def __gt__(self, other: "Comparable", /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def binary_search(arr: list[T], val: T) -> bool:
    """
    Performs a binary search to determine if a value exists in a sorted list.

    Args:
        arr: A sorted list of elements.
             Elements must support comparison operations.
        val: The value to search for in the list.

    Returns:
        True if the value is found in the list, False otherwise.
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
