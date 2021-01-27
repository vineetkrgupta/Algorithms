"""
Implementation of the min heap

Min heap is a data structure with the following property
parent <= children

- Min heap is usually implemented using an array
"""
import copy
from heapq import heapify
import unittest

class MinHeap(object):
    """Implementation of the min heap"""

    def __init__(self, input_list):
        self._heap = copy.copy(input_list)
        self._heapify()

    def _get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def _get_child_one_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 1

    def _get_child_two_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 2

    def _get_root_index(self) -> int:
        return 0

    def _get_last_child_index(self) -> int:
        return len(self._heap) - 1

    def _is_heap_property_satisfied(self, parent_index: int, child_index: int):
        return self._heap[parent_index] < self._heap[child_index]

    def _heapify(self):
        last_child = self._get_last_child_index()
        last_parent = self._get_parent_index(last_child)
        loop_boundary = -1

        # this heapify algorithm continuously sifts down all parents
        for curr_index in range(last_parent, loop_boundary, -1):
            self._sift_down(curr_index)

    def _sift_up(self, start_index: int):
        """Given an index, moves the child to parent until the heap property
        is satisfied"""

        child_index = start_index
        parent_index = self._get_parent_index(child_index, array)

        while not self._is_heap_property_satisfied(parent_index, child_index):
            self._swap(parent_index, child_index)
            child_index = parent_index
            parent_index = self._get_parent_index(child_index)

    def _sift_down(self, start_index: int):
        """Given a index, moves the parent to child until the heap property
        is satisfied or end_index is reached"""

        parent_index = start_index
        child_one_index = self._get_child_one_index(parent_index)
        last_child_index = self._get_last_child_index()

        while child_one_index <= last_child_index:
            child_two_index = self._get_child_two_index(parent_index)

            child_index_to_swap = min(
                child_one_index,
                child_two_index,
                key = lambda x: self._heap[x])

            if self._is_heap_property_satisfied(parent_index,
                child_index_to_swap):
                break
            
            self._swap(parent_index, child_index_to_swap)
            parent_index = child_index_to_swap
            child_one_index = self._get_child_one_index(parent_index)

    def _swap(self, index_i, index_j):
        self._heap[index_i], self._heap[index_j] =\
                self._heap[index_j], self._heap[index_i]

    def insert(self, value):
        """Insert a given value into the heap"""
        self._heap.append(value)
        last_child = self._get_last_child_index()
        self._sift_up(last_child)

    def remove(self):
        """Remove the minimum value in the heap"""
        
        root_index = self._get_root_index()
        last_child_index = self._get_last_child_index()
        self._swap(root_index, last_child_index)
        
        removed_element = self._heap.pop()
        self._sift_down(root_index)
        return removed_element

    def peek(self):
        """Returns the minimum value"""
        return self._heap[0]

    def get_heap(self):
        """Access the internal heap as array"""
        return self._heap

class TestMinHeap(unittest.TestCase):

    def test_build_heap(self):
        array = [2, 3, 1]
        heap = MinHeap(array)
        heapify(array)

        self.assertEqual(heap.get_heap(), array)

if __name__ == "__main__":
    unittest.main()
