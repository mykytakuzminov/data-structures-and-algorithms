from typing import Any, Optional


class Node:
    """
    Node class for a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: Pointer to the next node in the list.
    """
    data: Any
    next: Optional["Node"]

    def __init__(self, data: Any) -> None:
        """
        Initialize a node with a given value.

        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly Linked List implementation.

    This list allows traversal in only one direction (forward).
    It maintains a head pointer.

    Methods:
        append(data): Add an element to the end.
        prepend(data): Add an element to the beginning.
        insert(index, data): Insert at a specific index.
        delete(key): Remove the first occurrence of a value.
        search(key): Check if a value exists.
        get(index): Get value at a specific index.
        is_empty(): Check if the list is empty.
        clear(): Remove all elements.
        traverse(): Return a list of all elements.
    """
    _head: Optional[Node]
    _length: int

    def __init__(self) -> None:
        """Initialize an empty singly linked list."""
        self._head = None
        self._length = 0

    # --- Modification Methods (Insertion) ---

    def append(self, data: Any) -> None:
        """
        Add an element at the end of the list.

        Args:
            data: Value to append to the list.
        """
        new_node = Node(data)

        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node

        self._length += 1

    def prepend(self, data: Any) -> None:
        """
        Add an element at the beginning of the list.

        Args:
            data: The value to be added.
        """
        new_node = Node(data)

        new_node.next = self._head
        self._head = new_node

        self._length += 1

    def insert(self, index: int, data: Any) -> None:
        """
        Insert a new element at a specific index.

        Args:
            index: Position at which to insert the element.
            data: The value to be added.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self._head

        # Traverse to the node immediately before the index
        for _ in range(index - 1):
            if current:
                current = current.next

        if current:
            new_node.next = current.next
            current.next = new_node

        self._length += 1

    # --- Modification Methods (Deletion) ---

    def delete(self, key: Any) -> bool:
        """
        Delete the first element with the given value.

        Args:
            key: Value to delete.

        Returns:
            True if an element was deleted, False otherwise.
        """
        current = self._head
        prev = None

        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self._head = current.next

                self._length -= 1
                return True

            prev = current
            current = current.next

        return False

    def clear(self) -> None:
        """
        Remove all elements from the list.
        """
        self._head = None
        self._length = 0

    # --- Access & Search Methods ---

    def search(self, key: Any) -> bool:
        """
        Search for an element by value.

        Args:
            key: Value to search for.

        Returns:
            True if the element is found, False otherwise.
        """
        current = self._head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def get(self, index: int) -> Any:
        """
        Return the value of the node at a specific index.

        Args:
            index: Position of the element to retrieve.

        Returns:
            Value at the specified index.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        current = self._head
        for _ in range(index):
            if current:
                current = current.next

        if current:
            return current.data

        raise IndexError("Index out of range")

    def is_empty(self) -> bool:
        """
        Check if the list contains no elements.

        Returns:
            True if the list is empty, False otherwise.
        """
        return self._head is None

    def traverse(self) -> list[Any]:
        """
        Return a list of all elements in the linked list.

        Returns:
            A Python list containing all elements in order.
        """
        elements = []
        current = self._head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    # --- Internal/Testing Helpers ---

    def __len__(self) -> int:
        """
        Get the number of nodes in the list.

        Returns:
            The count of nodes.
        """
        return self._length

    def __str__(self) -> str:
        """
        Return a string representation of the list.

        Returns:
            String representation of the internal list.
        """
        return str(self.traverse())
