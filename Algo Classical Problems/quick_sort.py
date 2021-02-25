"""
Notes:
    - Quick sort is a simple algorithm that runs on average O(nlogn)
        1. Divide collection into roughly two equal parts using a pivot
        2. Elements larger than pivot move to the right of pivot and elements smaller than pivot
            move to the left.
        3. Repeat until the whole sequence is sorted

    - Unstable algorithm (Does not guarantee the positions of items stay the same.

References:
    - https://stackabuse.com/quicksort-in-python/
"""
import unittest

def rearrange_with_pivot(array, start, end):
    """move elements around pivot"""

    pivot = start
    left = start + 1
    right = end

    # arrage in such a way that lowest are below pivot
    # and highest are above pivot
    while left <= right:
        
        # if out of order swap (smaller should be left, bigger should be right)
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)

        # move forward until out of order
        if array[left] <= array[pivot]:
            left += 1

        # move backward until out of order
        if array[right] >= array[pivot]:
            right -= 1

    # after rearranging, put pivot in its place
    swap(array, pivot, right)

    return right

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def quick_sort(sequence, start, end):
    """Perform quick sort on the sequence in place"""
    
    if start >= end:
        return sequence

    mid = rearrange_with_pivot(sequence, start, end)
    quick_sort(sequence, start, mid - 1)
    quick_sort(sequence, mid + 1, end)

    return sequence

class TestQuickSort(unittest.TestCase):

    def test_empty(self):
        sequence = []
        self.assertEqual(quick_sort(sequence, 0, 0), [])

    def test_1(self):
        sequence = [4, 2, 3, 1, 2, 4]
        self.assertEqual(quick_sort(sequence, 0, len(sequence) -1), [1, 2, 2, 3, 4, 4])

    def test_basic_case(self):
        sequence = [ 5, 4, 3, 2, 1 ]
        self.assertEqual(quick_sort(sequence, 0, len(sequence) - 1), [ 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()


