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
    """
    _items: list[Any]

    def __init__(self) -> None:
        """Initialize an empty stack using a dynamic array."""
        self._items = []

    def push(self, item: Any) -> None:
        """Add an element to the top of the stack.

        Args:
            item: The value to be added.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element from the top of the stack.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top element of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack is empty, else False."""
        return len(self._items) == 0

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self._items.clear()

    def traverse(self) -> list[Any]:
        """Return a list of all elements in the stack."""
        return self._items

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._items)

    def __str__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack({self.traverse()})"
