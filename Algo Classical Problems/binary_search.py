"""
Binary search is a very important algorithm which enables the user to search for a specific item
by incrementally chopping the dataset in half. The search happens in O(logn) time and O(1) space.
The requirement is that the problem set has to be in a sorted order.
"""
import unittest
from typing import List


def binary_search(input_array: List[int], target: int):
    """
    Given a sorted input array of integers, the function looks for a target or returns None

    Returns:
        Target index or None
    """

    if not input_array or not target:
        return None

    left_pointer = 0
    right_pointer = len(input_array) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        mid_value = input_array[mid_pointer]

        if target > mid_value:
            left_pointer = mid_pointer + 1
        elif target < mid_value:
            right_pointer = mid_pointer - 1
        else:
            return mid_pointer

    return None

class TestBinarySearch(unittest.TestCase):

    def test_empty_seq(self):
        seq: List[int] = []
        target: int = 4

        self.assertEqual(binary_search(seq, target), None)

    def test_seq_with_one_item(self):
        seq: List[int] = [ 1 ]

        self.assertEqual(binary_search(seq, 4), None)
        self.assertEqual(binary_search(seq, 1), 0)

    def test_simple_seq(self):
        seq: List[int] = [ 1, 2, 3, 4, 5]
        target: int = 3

        self.assertEqual(binary_search(seq, target), 2)

if __name__ == "__main__":
    unittest.main()
