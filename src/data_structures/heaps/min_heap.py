from typing import Any
from src.data_structures.heaps.heap import Heap


class MinHeap(Heap):
    """Min-Heap implementation where the smallest element is at the root."""
    def _is_better(self, val1: Any, val2: Any) -> bool:
        return val1 > val2
