"""
Selection sort works by keeping markers for sorted and unsorted regions. 

1. On each iteration select the smallest element from unsorted region and 
put it in the sorted region.
"""
import unittest


def selection_sort(input_data):
    """Implementation of selection sort algorithm, Destroys the input data"""

    for unsorted_region_start in range(0, len(input_data)):
        curr_min_at = unsorted_region_start

        # find the smallest in unsorted region
        for curr_unsorted_index in range(unsorted_region_start + 1, len(input_data)):
            if input_data[curr_min_at] > input_data[curr_unsorted_index]:
                curr_min_at = curr_unsorted_index

        # now swap elements if indexes are different
        if curr_min_at != unsorted_region_start:
            input_data[curr_min_at], input_data[unsorted_region_start] =\
                input_data[unsorted_region_start], input_data[curr_min_at]


class TestSelectionSort(unittest.TestCase):

    def test_with_repetition(self):
        input_list = [5, 4, 3, 0, 2, 2, 1]
        expected_output = [0, 1, 2, 2, 3, 4, 5]
        selection_sort(input_list)
        
        self.assertEqual(input_list, expected_output)

    def test_empty(self):
        input_list = []
        expected_output = []
        selection_sort(input_list)
        self.assertEqual(input_list, expected_output)

    def test_all_reverse(self):
        input_list = [5, 4, 3, 2, 1]
        expected_output = [1, 2, 3, 4, 5]
        selection_sort(input_list)
        self.assertEqual(input_list, expected_output)

    def test_already_sorted(self):
        input_list = [ 1, 2, 3, 4, 5]
        expected_output = [ 1, 2, 3, 4, 5]
        selection_sort(input_list)
        self.assertEqual(input_list, expected_output)
        


if __name__ == "__main__":
    unittest.main()
