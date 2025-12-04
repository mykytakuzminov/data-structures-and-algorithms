from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def selection_sort(arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort divides the input list into two sublists: a sorted sublist
    built up from the front and the remaining unsorted sublist. It repeatedly
    finds the minimum element from the unsorted sublist and swaps it with the
    first element of the unsorted sublist (which is also the element at the
    boundary of the sorted sublist). It is an in-place sorting algorithm.

    Complexity:
        - Best Case (already sorted): O(n^2)
        - Average Case: O(n^2)
        - Worst Case (reverse sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
