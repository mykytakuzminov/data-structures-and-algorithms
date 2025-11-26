from typing import Any
from src.data_structures.linked_lists.doubly_linked_list import (
    DoublyLinkedList,
)


class Queue:
    """
    Queue data structure implemented using a doubly linked list.

    The queue follows the FIFO (First In, First Out) principle.
    Elements are added to the back and removed from the front.

    Methods:
        enqueue(item): Add an element to the end of the queue.
        dequeue(): Remove and return the element from the front.
        front(): Return the first element without removing it.
        back(): Return the last element without removing it.
        is_empty(): Check if the queue is empty.
        clear(): Remove all elements from the queue.
        traverse(): Return a list of all elements.
    """
    _items: DoublyLinkedList

    def __init__(self) -> None:
        """Initialize an empty queue using a doubly linked list."""
        self._items = DoublyLinkedList()

    # --- Modification Methods ---

    def enqueue(self, item: Any) -> None:
        """
        Add an element to the end of the queue.

        Args:
            item: The value to be added.
        """
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the element from the front of the queue.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.pop_front()

    def clear(self) -> None:
        """
        Remove all elements from the queue.
        """
        self._items.clear()

    # --- Access & Status Methods ---

    def front(self) -> Any:
        """
        Return the first element of the queue without removing it.

        Returns:
            The value at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.peek_front()

    def back(self) -> Any:
        """
        Return the last element of the queue without removing it.

        Returns:
            The value at the back of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.peek_back()

    def is_empty(self) -> bool:
        """
        Check if the queue contains no elements.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self._items.is_empty()

    # --- Traversal & Helpers ---

    def traverse(self) -> list[Any]:
        """
        Return a list of all elements in the queue.

        Returns:
            A list containing all elements currently in the queue.
        """
        return self._items.traverse()

    def __len__(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            The count of items in the queue.
        """
        return len(self._items)

    def __str__(self) -> str:
        """
        Return a string representation of the queue.

        Returns:
            String in format 'Queue([item1, item2, ...])'
        """
        return f"Queue({self.traverse()})"
