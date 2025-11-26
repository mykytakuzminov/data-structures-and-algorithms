from typing import Any


class Stack:
    """
    Stack data structure implemented using a dynamic array (Python list).

    The stack follows the LIFO (Last In, First Out) principle.
    Elements are added and removed from the top of the stack.

    Methods:
        push(item): Add an element to the top of the stack.
        pop(): Remove and return the element from the top.
        peek(): Return the top element without removing it.
        is_empty(): Check if the stack is empty.
        clear(): Remove all elements from the stack.
        traverse(): Return a list of all elements.
    """
    _items: list[Any]

    def __init__(self) -> None:
        """Initialize an empty stack using a dynamic array."""
        self._items = []

    # --- Modification Methods ---

    def push(self, item: Any) -> None:
        """
        Add an element to the top of the stack.

        Args:
            item: The value to be added.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the element from the top of the stack.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        """
        self._items.clear()

    # --- Access & Status Methods ---

    def peek(self) -> Any:
        """
        Return the top element of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack contains no elements.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    # --- Traversal & Helpers ---

    def traverse(self) -> list[Any]:
        """
        Return a copy of all elements in the stack.

        Returns:
            A list containing all elements currently in the stack.
        """
        return list(self._items)

    def __len__(self) -> int:
        """
        Get the number of elements in the stack.

        Returns:
            The count of items in the stack.
        """
        return len(self._items)

    def __str__(self) -> str:
        """
        Return a string representation of the stack.

        Returns:
            String in format 'Stack([item1, item2, ...])'
        """
        return f"Stack({self.traverse()})"
