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


def factorial(n: int) -> int:
    """
    Compute the factorial of a number recursively.

    Args:
        n: Non-negative integer whose factorial to compute.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.

    Returns:
        Factorial of n.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == (0, 1):
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Compute the n-th Fibonacci number recursively.

    Args:
        n: Index (non-negative) of the Fibonacci sequence.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.

    Returns:
        int: The n-th Fibonacci number.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}.")

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_nested_list(arr: list[int | float | list]) -> int | float:
    """
    Recursively compute the sum of all numbers in a nested list.

    Args:
        arr: List that may contain integers, floats, or other nested lists.

    Raises:
        TypeError: If an element is neither a number nor a list.

    Returns:
        The total sum of all numeric elements.
    """
    result: int | float = 0
    for el in arr:
        if isinstance(el, list):
            result += sum_nested_list(el)
        elif isinstance(el, (int, float)):
            result += el
        else:
            raise TypeError(f"Unsupported element type: {type(el).__name__}")

    return result
