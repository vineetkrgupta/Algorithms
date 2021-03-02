"""
Insertion sort is one of the simple sorting algorithms. The efficiency is not that good compared
to other sorting algorithms but the simplicity is very evident.
"""
import unittest


def insertion_sort(input_data):
    """Implementation of the insertion sort algorithm to sort data. The sorting is done in-place so
    be careful."""

    for curr_sorted_index in range(0, len(input_data)):

        # we maintain a sorted region and unsorted region within the data
        # starting from 0 to curr_sorted_index - sorted area
        for inner_index in range(curr_sorted_index, 0, -1):
            inner_element = input_data[inner_index]

            # NOTE - be careful here with inner_index as we access prev index (-1)
            prev_inner_index = inner_index - 1
            prev_inner_element = input_data[prev_inner_index]

            if prev_inner_element > inner_element:
                swap_elements(input_data, inner_index, prev_inner_index)


def swap_elements(input_data, index_a, index_b):
    input_data[index_a], input_data[index_b] = input_data[index_b], input_data[index_a]


class TestInsertionSort(unittest.TestCase):

    def test_simple_case(self):
        input_list = [5, 4, 3, 2, 2, 1]
        expected_output = [1, 2, 2, 3, 4, 5]

        insertion_sort(input_list)

        self.assertEqual(input_list, expected_output)


if __name__ == "__main__":
    unittest.main()
