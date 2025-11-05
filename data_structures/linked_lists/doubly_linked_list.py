class Node:
    """
    Node class for doubly linked list
    """
    def __init__(self, data):
        """Initialize a node with a given value"""
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly linked list with basic operations
    """
    def __init__(self):
        """Initialize an empty doubly linked list"""
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        """Return the number of nodes in the list"""
        return self._length

    def __str__(self):
        """Return a string representation of the list"""
        return str(self.traverse())

    def is_empty(self):
        """Check if the list is empty"""
        return self._head is None

    def append(self, data):
        """Add an element at the end of the list"""
        new_node = Node(data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._length += 1

    def prepend(self, data):
        """Add an element at the beginning of the list"""
        new_node = Node(data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._length += 1

    def insert(self, index, data):
        """Insert a new element at a specific index"""
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self._length:
            self.append(data)
            return

        new_node = Node(data)

        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                current = current.prev

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self._length += 1

    def delete(self, key):
        """Delete the first element with the given value"""
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

    def search(self, key):
        """Search for an element by value"""
        current = self._head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def get(self, index):
        """Return the value of node at specific index"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                current = current.prev
        return current.data

    def traverse(self):
        """Return a list of all elements in the linked list"""
        elements = []
        current = self._head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def clear(self):
        """Remove all elements from the list"""
        self._head = None
        self._tail = None
        self._length = 0

    def _get_head(self):
        """Return the head of the list for testing"""
        return self._head

    def _get_tail(self):
        """Return the tail of the list for testing"""
        return self._tail
