"""
Given a sequence of numbers in ascending to descending/descending to ascending order find the 
rotation point.
"""
import unittest

def find_rotation_point(sequence):
    """Returns the index of the rotation"""

    if not sequence:
        return sequence

    left = 0
    right = len(sequence) - 1
    first = sequence[0]

    # TODO: This algorithm only works for sequence that is strictly decreasing & increasing

    while left <= right:

        mid = (left + right) // 2
        
        if sequence[mid] >= first:
            left = mid
        else:
            right = mid

        if left + 1 == right:
            return right
    
    return right 
            
class TestFindRotationPoint(unittest.TestCase):

    def test_increasing_at_center(self):
        self.assertEqual(
            find_rotation_point([4, 3, 2, 1, 2, 3, 4]),
            3
        )

    def test_increasing_at_start(self):
        self.assertEqual(
            find_rotation_point([5, 1, 2, 3, 4]),
            1
        )

    def test_decreasing_at_end(self):
        self.assertEqual(
            find_rotation_point([5, 4, 3, 2, 1, 2]),
            4
        )

    def test_decreasing_at_center(self):
        self.assertEqual(
            find_rotation_point([1, 2, 3, 4, 3, 2, 1]),
            3
        )
        
    def test_strictly_decreasing(self):
        self.assertEqual(
            find_rotation_point([5, 4, 3, 2, 1]),
            4
        )

    def test_strictly_increasing(self):
        self.assertEqual(
            find_rotation_point([1, 2, 3, 4, 5]),
            0
        )

if __name__ == "__main__":
    unittest.main()
