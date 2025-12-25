from typing import Any
from src.data_structures.queues.queue import Queue
from src.data_structures.stacks.stack import Stack


class Node:
    """
    A node in a graph.

    Attributes:
        value: The data stored in the node.
        neighbors: A set of references to neighboring Node objects.
    """
    value: Any
    neighbors: set["Node"]

    def __init__(self, value: Any):
        """
        Initialize a graph node.

        Args:
            value: The data to store in the node.
        """
        self.value = value
        self.neighbors = set()


class Graph:
    """
    Graph implementation using an adjacency list (dictionary of Nodes).

    This data structure represents a collection of nodes and their connections.
    It supports both directed and undirected edges and provides methods for
    graph traversal (BFS, DFS).

    Methods:
        add_node(value): Add a new node to the graph.
        add_edge(val1, val2, directed): Create a connection between two nodes.
        remove_node(value): Remove a node and all its associated edges.
        remove_edge(val1, val2, directed): Remove a connection between nodes.
        get_neighbors(value): Return a list of values of neighboring nodes.
        has_edge(val1, val2): Check if a connection exists between two nodes.
        bfs(start_value): Perform a Breadth-First Search traversal.
        dfs(start_value): Perform a Depth-First Search traversal.
        size: Property returning the number of nodes in the graph.
        is_empty: Property checking if the graph has no nodes.
    """
    _adj_list: dict[Any, Node]

    def __init__(self) -> None:
        """
        Initialize an empty graph.
        """
        self._adj_list = {}

    @property
    def size(self) -> int:
        """
        Return the total number of nodes in the graph.

        Returns:
            The number of nodes.
        """
        return len(self._adj_list)

    @property
    def is_empty(self) -> bool:
        """
        Check if the graph contains no nodes.

        Returns:
            True if empty, False otherwise.
        """
        return self.size == 0

    # --- Modification Methods ---

    def add_node(self, value: Any) -> None:
        """
        Add a new node to the graph if it does not already exist.

        Args:
            value: The value to be added as a node.
        """
        if value not in self._adj_list:
            self._adj_list[value] = Node(value)

    def add_edge(self, val1: Any, val2: Any, directed: bool = False) -> None:
        """
        Add an edge between two nodes. Nodes are created if they don't exist.

        Args:
            val1: The value of the first node.
            val2: The value of the second node.
            directed: If True, the edge is one-way (val1 -> val2).
                      Default is False (undirected).
        """
        self.add_node(val1)
        self.add_node(val2)

        node1 = self._adj_list[val1]
        node2 = self._adj_list[val2]

        node1.neighbors.add(node2)
        if not directed:
            node2.neighbors.add(node1)

    def remove_node(self, value: Any) -> None:
        """
        Remove a node and all edges connected to it from the graph.

        Args:
            value: The value of the node to remove.
        """
        if value not in self._adj_list:
            return

        target_node = self._adj_list[value]

        # Cleanup: remove this node from all other nodes' neighbor sets
        for node in self._adj_list.values():
            node.neighbors.discard(target_node)

        del self._adj_list[value]

    def remove_edge(self, val1: Any, val2: Any, directed: bool = False) -> None:
        """
        Remove an edge between two nodes.

        Args:
            val1: The value of the starting node.
            val2: The value of the ending node.
            directed: If True, only remove the directed edge val1 -> val2.
                      Default is False.
        """
        if val1 not in self._adj_list or val2 not in self._adj_list:
            return

        node1 = self._adj_list[val1]
        node2 = self._adj_list[val2]

        node1.neighbors.discard(node2)
        if not directed:
            node2.neighbors.discard(node1)

    # --- Access & Search Methods ---

    def get_neighbors(self, value: Any) -> list[Any]:
        """
        Return a list of values for all neighbors of a given node.

        Args:
            value: The node to get neighbors for.

        Returns:
            A list of values of the neighboring nodes.
        """
        if value not in self._adj_list:
            return []

        return [neighbor.value for neighbor in self._adj_list[value].neighbors]

    def has_edge(self, val1: Any, val2: Any) -> bool:
        """
        Check if there is an edge between two nodes.

        Args:
            val1: The starting node value.
            val2: The ending node value.

        Returns:
            True if the edge exists, False otherwise.
        """
        if val1 not in self._adj_list or val2 not in self._adj_list:
            return False

        return self._adj_list[val2] in self._adj_list[val1].neighbors

    # --- Traversal Methods ---

    def bfs(self, start_value: Any) -> list[Any]:
        """
        Perform a Breadth-First Search (BFS) starting from the given node.

        Args:
            start_value: The value of the node to start the traversal.

        Returns:
            A list of node values in BFS order.
        """
        if start_value not in self._adj_list:
            return []

        result = []
        seen = {start_value}
        queue = Queue()
        queue.enqueue(self._adj_list[start_value])

        while not queue.is_empty():
            curr_node = queue.dequeue()
            result.append(curr_node.value)

            for neighbor in sorted(curr_node.neighbors, key=lambda x: x.value):
                if neighbor.value not in seen:
                    seen.add(neighbor.value)
                    queue.enqueue(neighbor)

        return result

    def dfs(self, start_value: Any) -> list[Any]:
        """
        Perform a Depth-First Search (DFS) starting from the given node.

        Args:
            start_value: The value of the node to start the traversal.

        Returns:
            A list of node values in DFS order.
        """
        if start_value not in self._adj_list:
            return []

        result = []
        seen = set()
        stack = Stack()
        stack.push(self._adj_list[start_value])

        while not stack.is_empty():
            curr_node = stack.pop()

            if curr_node.value not in seen:
                seen.add(curr_node.value)
                result.append(curr_node.value)

                sorted_neighbors = sorted(
                    curr_node.neighbors,
                    key=lambda x: x.value,
                    reverse=True
                )

                for neighbor in sorted_neighbors:
                    if neighbor.value not in seen:
                        stack.push(neighbor)

        return result
