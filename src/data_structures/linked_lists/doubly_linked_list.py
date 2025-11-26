from typing import Any, Optional


class Node:
    """
    Node class for a doubly linked list.

    Attributes:
        data: The value stored in the node.
        next: Pointer to the next node in the list.
        prev: Pointer to the previous node in the list.
    """
    data: Any
    next: Optional["Node"]
    prev: Optional["Node"]

    def __init__(self, data: Any) -> None:
        """
        Initialize a node with a given value.

        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation.

    This list allows traversal in both directions (forward and backward).
    It maintains a head and a tail pointer for O(1) insertions at both ends.

    Methods:
        append(data): Add an element to the end.
        prepend(data): Add an element to the beginning.
        insert(index, data): Insert at a specific index.
        delete(key): Remove the first occurrence of a value.
        pop_front(): Remove and return the first element.
        search(key): Check if a value exists.
        get(index): Get value at a specific index.
        peek_front(): Get the first value without removing.
        peek_back(): Get the last value without removing.
        is_empty(): Check if the list is empty.
        clear(): Remove all elements.
        traverse(): Return a list of all elements.
    """
    _head: Optional[Node]
    _tail: Optional[Node]
    _length: int

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self._head = None
        self._tail = None
        self._length = 0

    # --- Modification Methods (Insertion) ---

    def append(self, data: Any) -> None:
        """
        Add an element at the end of the list (Tail).

        Args:
            data: The value to be added.
        """
        new_node = Node(data)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            if self._tail:
                self._tail.next = new_node
                new_node.prev = self._tail
                self._tail = new_node

        self._length += 1

    def prepend(self, data: Any) -> None:
        """
        Add an element at the beginning of the list (Head).

        Args:
            data: The value to be added.
        """
        new_node = Node(data)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
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
        if index == self._length:
            self.append(data)
            return

        new_node = Node(data)

        # Optimization: Decide traversal direction (start from head or tail)
        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                if current:
                    current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                if current:
                    current = current.prev

        # Current is now the node that will be *after* the new node
        if current and current.prev:
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

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
        while current:
            if current.data == key:
                # If it's not the head
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                # If it's not the tail
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev

                self._length -= 1
                return True

            current = current.next

        return False

    def pop_front(self) -> Any:
        """
        Remove and return the element at the head of the list.

        Returns:
            The value of the removed node.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty() or self._head is None:
            raise IndexError("List is empty")

        value = self._head.data
        self._head = self._head.next

        if self._head:
            self._head.prev = None
        else:
            # List became empty
            self._tail = None

        self._length -= 1
        return value

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

        # Optimization: Traverse from nearest end
        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                if current:
                    current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                if current:
                    current = current.prev

        if current:
            return current.data

        raise IndexError("Index out of range")

    def peek_front(self) -> Any:
        """
        Return the value of the head node without removing it.

        Returns:
            The value at the front.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty() or self._head is None:
            raise IndexError("List is empty")
        return self._head.data

    def peek_back(self) -> Any:
        """
        Return the value of the tail node without removing it.

        Returns:
            The value at the back.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty() or self._tail is None:
            raise IndexError("List is empty")
        return self._tail.data

    # --- Status & Utility Methods ---

    def is_empty(self) -> bool:
        """
        Check if the list contains no elements.

        Returns:
            True if the list is empty, False otherwise.
        """
        return self._head is None

    def clear(self) -> None:
        """
        Remove all elements from the list.
        """
        self._head = None
        self._tail = None
        self._length = 0

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

    def _get_head(self) -> Node | None:
        """Return the head node (for internal testing)."""
        return self._head

    def _get_tail(self) -> Node | None:
        """Return the tail node (for internal testing)."""
        return self._tail

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
