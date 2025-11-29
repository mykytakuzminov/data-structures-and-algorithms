from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def bubble_sort(arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the optimized Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This implementation includes
    an optimization to stop early if a pass completes without any swaps.
    It is an in-place sorting algorithm.

    Complexity:
        - Best Case (already sorted): O(n)
        - Average Case: O(n^2)
        - Worst Case (reverse sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
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
