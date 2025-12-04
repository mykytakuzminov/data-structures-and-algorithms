from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def merge_sort(arr: list[T]) -> list[T]:
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Merge Sort is a Divide and Conquer algorithm. It recursively divides the
    list into halves until they contain only one element (which is sorted),
    and then merges those sublists to form a new sorted list.

    Complexity:
        - Best Case: O(n log n)
        - Average Case: O(n log n)
        - Worst Case: O(n log n)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).

    Returns:
        A new list containing the sorted elements. (Note: This is not an in-place sort.)
    """
    n = len(arr)

    if n <= 1:
        return arr

    m = n // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)

    sorted_arr: list[T] = []

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr.append(L[l])
            l += 1
        else:
            sorted_arr.append(R[r])
            r += 1

    sorted_arr.extend(L[l:])
    sorted_arr.extend(R[r:])

    return sorted_arr
