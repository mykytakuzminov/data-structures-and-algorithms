from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList

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
    """
    def __init__(self):
        """Initialize an empty queue using a doubly linked list."""
        self._dll = DoublyLinkedList()

    def enqueue(self, item):
        """Add an element to the end of the queue.

        Args:
            item: The value to be added.
        """
        self._dll.append(item)

    def dequeue(self):
        """Remove and return the element from the front of the queue.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the queue is empty.
        """
        try:
            return self._dll.pop_front()
        except IndexError:
            raise IndexError("Queue is empty")

    def front(self):
        """Return the first element of the queue without removing it.

        Returns:
            The value at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        try:
            return self._dll.peek_front()
        except IndexError:
            raise IndexError("Queue is empty")

    def back(self):
        """Return the last element of the queue without removing it.

        Returns:
            The value at the back of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        try:
            return self._dll.peek_back()
        except IndexError:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """Return True if the queue is empty, else False."""
        return self._dll.is_empty()

    def clear(self):
        """Remove all elements from the queue."""
        self._dll.clear()

    def traverse(self):
        """Return a list of all elements in the queue."""
        return self._dll.traverse()

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._dll)

    def __str__(self):
        """Return a string representation of the queue."""
        return f"Queue({self.traverse()})"
