from typing import Any


def sum(arr: list[int | float]) -> int | float:
    """
    Recursively calculates the sum of all numeric elements in a list.

    Args:
        arr: A list of integers or floats.

    Raises:
        TypeError: If any element in the list is not numeric.

    Returns:
        The sum of all elements in the list. Returns 0 if the list is empty.
    """
    if not arr:
        return 0

    if not isinstance(arr[0], (int, float)):
        raise TypeError(f"Expected number, got {type(arr[0]).__name__}.")

    return arr[0] + sum(arr[1:])


def max(arr: list[int | float]) -> int | float:
    """
    Recursively determines the maximum element in a list.

    Args:
        arr: A list of integers or floats.

    Raises:
        ValueError: If the list is empty.
        TypeError: If any element in the list is not numeric.

    Returns:
        The maximum element in the list.
    """
    if not arr:
        raise ValueError("Expected a non-empty list, got an empty list.")

    if not isinstance(arr[0], (int, float)):
        raise TypeError(f"Expected number, got {type(arr[0]).__name__}.")

    if len(arr) == 1:
        return arr[0]

    rest_max = max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max


def reverse(arr: list[Any]) -> list[Any]:
    """
    Recursively returns a new list with elements in reverse order.

    Args:
        arr: A list of any elements.

    Returns:
        A new list containing the elements of the input list in reverse order.
    """
    if not arr:
        return []

    return [arr[-1]] + reverse(arr[:-1])
