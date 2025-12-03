from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)

def insertion_sort(arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Insertion Sort builds the final sorted list one item at a time. It iterates
    through the input elements and inserts each element into its correct position
    in the already-sorted part of the array.
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

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
