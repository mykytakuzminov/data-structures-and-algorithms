from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def bubble_sort(arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    This is an in-place sort with O(n^2) time complexity.
    It includes an optimization to stop early if the list is already sorted.

    Args:
        arr: A list of elements that support comparison operations.
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        if not swapped:
            break
