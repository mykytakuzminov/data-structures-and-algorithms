from typing import TypeVar, Protocol, Any


class Comparable(Protocol):
    """Protocol for objects that support comparison operations."""
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


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


def quick_sort(arr: list[T]) -> list[T]:
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Quick Sort is a highly efficient, comparison-based sorting algorithm that
    uses a Divide and Conquer strategy. It works by selecting a 'pivot' element
    from the array and partitioning the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot. The
    sub-arrays are then recursively sorted.

    Complexity:
        - Best Case (optimal pivot choice): O(n log n)
        - Average Case: O(n log n)
        - Worst Case (poor pivot choice, e.g., already sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).

    Returns:
        A new list containing the sorted elements. (Note: This is not an in-place sort.)
    """
    n = len(arr)

    if n <= 1:
        return arr

    p = arr[-1]

    L = [n for n in arr[:-1] if n <= p]
    R = [n for n in arr[:-1] if n > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R
