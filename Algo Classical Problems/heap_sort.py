"""
Notes:
    - Efficient sorting algorithm.
    - Requires knowledge on arrays and trees.
    - Uses a heap data structure (Complete Binary Tree)

Applications:
    - Heap sort is used in many algorithms as intermediate step.

Links:
    - https://www.programiz.com/dsa/heap-sort
"""
from typing import List
import unittest

def heap_sort(input: List[int]):
    """Implementation of heap sort using built-in heapify function"""
   
    # Build a max heap
    # Swap root with the last element
    # Remove root
    # Repeat process unitl all items are sorted
    pass

class TestHeapSort(self):

    def test_descending_order(self):
        input = [ 5, 4, 3, 2, 1]
        output = [ 1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(input), output)

if __name__ == "__main__":
    unittest.main()
    
    
