from typing import Any, Optional


class Node:
    """
    Node class for doubly linked list.

    Attributes:
        data: The value stored in the node.
        next: Pointer to the next node in the list.
        prev: Pointer to the previous node in the list.
    """
    data: Any
    next: Optional["Node"]
    prev: Optional["Node"]

    def __init__(self, data: Any):
        """Initialize a node with a given value."""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly linked list with basic operations.

    Methods:
        is_empty(): Check if the list is empty.
        append(data): Add an element at the end of the list.
        prepend(data): Add an element at the beginning of the list.
        insert(index, data): Insert element at a specific index.
        delete(key): Delete the first element with the given value.
        search(key): Search for an element by value.
        get(index): Get value at a specific index.
        traverse(): Return all elements as a list.
        clear(): Remove all elements from the list.
    """
    _head: Optional[Node]
    _tail: Optional[Node]
    _length: int

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self._head = None
        self._tail = None
        self._length = 0

    def is_empty(self) -> bool:
        """Return True if the list is empty, else False."""
        return self._head is None

    def append(self, data: Any) -> None:
        """Add an element at the end of the list.

        Args:
            data: The value to be added.
        """
        new_node = Node(data)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            assert self._tail is not None
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

        self._length += 1

    def prepend(self, data: Any) -> None:
        """Add an element at the beginning of the list.

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
        """Insert a new element at a specific index.

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

        # Decide traversal direction for efficiency
        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                assert current is not None
                current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                assert current is not None
                current = current.prev

        assert current is not None
        assert current.prev is not None

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self._length += 1

    def delete(self, key: Any) -> bool:
        """Delete the first element with the given value.

        Args:
            key: Value to delete.

        Returns:
            True if an element was deleted, False otherwise.
        """
        current = self._head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev

                self._length -= 1
                return True

            current = current.next

        return False

    def search(self, key: Any) -> bool:
        """Search for an element by value.

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
        """Return the value of node at a specific index.

        Args:
            index: Position of the element to retrieve.

        Returns:
            Value at the specified index.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                assert current is not None
                current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                assert current is not None
                current = current.prev

        assert current is not None

        return current.data

    def traverse(self) -> list[Any]:
        """Return a list of all elements in the linked list."""
        elements = []
        current = self._head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def clear(self) -> None:
        """Remove all elements from the list."""
        self._head = None
        self._tail = None
        self._length = 0

    def pop_front(self) -> Any:
        """Remove and return the element at the head of the list."""
        if self._head is None:
            raise IndexError("List is empty")

        value = self._head.data
        self._head = self._head.next

        if self._head:
            self._head.prev = None
        else:
            self._tail = None

        self._length -= 1
        return value

    def peek_front(self) -> Any:
        """Return the value of the head node without removing it."""
        if self._head is None:
            raise IndexError("List is empty")
        return self._head.data

    def peek_back(self) -> Any:
        """Return the value of the tail node without removing it."""
        if self._tail is None:
            raise IndexError("List is empty")
        return self._tail.data

    def _get_head(self) -> Node | None:
        """Return the head node (for testing purposes)."""
        return self._head

    def _get_tail(self) -> Node | None:
        """Return the tail node (for testing purposes)."""
        return self._tail

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self._length

    def __str__(self) -> str:
        """Return a string representation of the list."""
        return str(self.traverse())
