"""
The following program finds the largest three numbers in a given array of numbers
"""
import heapq
import unittest
from typing import List


def find_largest_three(input_list: List[int]):
    """Returns the largest three numbers in sorted order"""

    buffer = [float("-inf")] * 3

    for number in input_list:
        heapq.heapreplace(buffer, number)

    return sorted(buffer)


class FindLargestThreeTest(unittest.TestCase):

    def test_simple_array(self):
        self.assertEqual(find_largest_three([3, 45, 2]), [2, 3, 45])

    def test_list_with_same_numbers(self):
        self.assertEqual(find_largest_three([3, 3, 4]), [3, 3, 4])


if __name__ == "__main__":
    unittest.main()
