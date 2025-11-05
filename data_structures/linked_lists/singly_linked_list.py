class Node:
    """
    Node class for singly linked list.

    Attributes:
        data: The value stored in the node.
        next: Pointer to the next node in the list.
    """
    def __init__(self, data):
        """Initialize a node with a given value."""
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list with basic operations.

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
    def __init__(self):
        """Initialize an empty singly linked list."""
        self._head = None
        self._length = 0

    def is_empty(self):
        """Return True if the list is empty, else False."""
        return self._head is None

    def append(self, data):
        """Add an element at the end of the list.

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

    def prepend(self, data):
        """Add an element at the beginning of the list.

        Args:
            data: Value to prepend to the list.
        """
        new_node = Node(data)

        new_node.next = self._head
        self._head = new_node

        self._length += 1

    def insert(self, index, data):
        """Insert a new element at a specific index.

        Args:
            index: Position at which to insert the element.
            data: Value to insert.

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
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self._length += 1

    def delete(self, key):
        """Delete the first element with the given value.

        Args:
            key: Value to delete from the list.

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

    def search(self, key):
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

    def get(self, index):
        """Return the value of the node at a specific index.

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
            current = current.next

        return current.data

    def traverse(self):
        """Return a list of all elements in the linked list."""
        elements = []
        current = self._head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def clear(self):
        """Remove all elements from the list."""
        self._head = None
        self._length = 0

    def __len__(self):
        """Return the number of nodes in the list."""
        return self._length

    def __str__(self):
        """Return a string representation of the list."""
        return str(self.traverse())
