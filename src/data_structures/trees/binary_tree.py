from typing import Any, Optional
from src.data_structures.queues.queue import Queue
from src.data_structures.stacks.stack import Stack


class TreeNode:
    """
    Represents a node in a Binary Tree.

    Attributes:
        data: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    data: Any
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, data: Any) -> None:
        """
        Initialize a tree node.

        Args:
            data: The value to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Search Tree (BST) implementation.

    This data structure organizes data in a hierarchical tree structure.
    For any given node, elements in the left subtree are smaller,
    and elements in the right subtree are larger.

    Methods:
        insert(data): Add a new element to the tree maintaining BST property.
        search(data): Check if an element exists in the tree.
        is_empty(): Check if the tree is empty.
        height(): Return the height (max depth) of the tree.
        size(): Return the total number of nodes in the tree.
        preorder_iterative(): Perform preorder traversal (Root -> Left -> Right).
        inorder_iterative(): Perform inorder traversal (Left -> Root -> Right).
        postorder_iterative(): Perform postorder traversal (Left -> Right -> Root).
        level_order(): Perform breadth-first traversal (level by level).
    """
    _root: Optional[TreeNode]

    def __init__(self) -> None:
        """Initialize an empty Binary Tree."""
        self._root = None

    # --- Modification Methods ---

    def insert(self, data: Any) -> None:
        """
        Insert a new element into the Binary Search Tree.

        If the root is empty, the new data becomes the root.
        Otherwise, it recursively finds the correct position.

        Args:
            data: The value to be added to the tree.
        """
        if self._root is None:
            self._root = TreeNode(data)
        else:
            self._insert_recursive(self._root, data)

    # --- Query & Status Methods ---

    def search(self, data: Any) -> bool:
        """
        Search for a specific value in the tree iteratively.

        Args:
            data: The value to search for.

        Returns:
            True if the data exists in the tree, False otherwise.
        """
        root = self._root

        while root is not None:
            if data == root.data:
                return True
            elif data < root.data:
                root = root.left
            else:
                root = root.right

        return False

    def is_empty(self) -> bool:
        """
        Check if the tree contains no elements.

        Returns:
            True if the tree is empty, False otherwise.
        """
        return self._root is None

    def height(self) -> int:
        """
        Calculate the height of the tree.

        The height is defined as the number of edges on the longest
        path from the root to a leaf node.

        Returns:
            The height of the tree (0 if empty).
        """
        if self._root is None:
            return 0

        return self._height(self._root)

    def size(self) -> int:
        """
        Calculate the total number of nodes in the tree.

        Returns:
            The total count of nodes.
        """
        if self._root is None:
            return 0

        return self._size(self._root)

    # --- Traversal Methods ---

    def preorder_iterative(self) -> list[Any]:
        """
        Perform an iterative preorder traversal (Root -> Left -> Right).

        Returns:
            A list of elements in preorder sequence.
        """
        if self._root is None:
            return []

        stack: Stack = Stack()
        stack.push(self._root)
        result: list[Any] = []

        while not stack.is_empty():
            tree_node: TreeNode = stack.pop()
            result.append(tree_node.data)

            if tree_node.right:
                stack.push(tree_node.right)
            if tree_node.left:
                stack.push(tree_node.left)

        return result

    def inorder_iterative(self) -> list[Any]:
        """
        Perform an iterative inorder traversal (Left -> Root -> Right).

        For a BST, this returns elements in sorted ascending order.

        Returns:
            A list of elements in inorder sequence.
        """
        stack: Stack = Stack()
        result: list[Any] = []
        root = self._root

        while root or not stack.is_empty():

            while root:
                stack.push(root)
                root = root.left

            root = stack.pop()
            result.append(root.data)

            root = root.right

        return result

    def postorder_iterative(self) -> list[Any]:
        """
        Perform an iterative postorder traversal (Left -> Right -> Root).

        Returns:
            A list of elements in postorder sequence.
        """
        stack: Stack = Stack()
        result: list[Any] = []
        root = self._root
        last_visited: Optional[TreeNode] = None

        while root or not stack.is_empty():

            while root:
                stack.push(root)
                root = root.left

            root = stack.peek()

            if not root.right or last_visited == root.right:
                result.append(root.data)
                last_visited = stack.pop()
                root = None
            else:
                root = root.right

        return result

    def level_order(self) -> list[Any]:
        """
        Perform a level-order traversal (Breadth-First Search).

        Returns:
            A list of elements level by level, from left to right.
        """
        if self._root is None:
            return []

        queue: Queue = Queue()
        queue.enqueue(self._root)
        result: list[Any] = []

        while not queue.is_empty():
            tree_node = queue.dequeue()
            result.append(tree_node.data)

            if tree_node.left:
                queue.enqueue(tree_node.left)
            if tree_node.right:
                queue.enqueue(tree_node.right)

        return result

    # --- Private Helper Methods ---

    def _insert_recursive(self, root: TreeNode, data: Any) -> None:
        """
        Helper method to recursively insert data into the BST.
        """
        if data < root.data:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                self._insert_recursive(root.left, data)

        elif data > root.data:
            if root.right is None:
                root.right = TreeNode(data)
            else:
                self._insert_recursive(root.right, data)

    def _height(self, root: Optional[TreeNode]) -> int:
        """
        Helper method to recursively calculate the height.
        """
        if root is None:
            return 0

        return 1 + max(self._height(root.left), self._height(root.right))

    def _size(self, root: Optional[TreeNode]) -> int:
        """
        Helper method to recursively calculate the size.
        """
        if root is None:
            return 0

        return 1 + self._size(root.left) + self._size(root.right)
