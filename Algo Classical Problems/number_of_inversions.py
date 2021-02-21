"""
Given a list of numbers, find the number of inversions required to get them in order

(Divide and conquer)
"""
import unittest


def sort_and_count(array, running_count=0):
    """Uses the merge sort algorithm to sort and count recursively"""

    # base case
    if len(array) <= 1:
        return (array, running_count)

    mid_ptr = len(array) // 2

    sorted_b, count_a = sort_and_count(array[:mid_ptr], running_count)
    sorted_c, count_b = sort_and_count(array[mid_ptr:], running_count)

    running_count += count_a
    running_count += count_b

    merged_array, count = merge_and_count(sorted_b, sorted_c)
    running_count += count

    return (merged_array, running_count)


def merge_and_count(array_b, array_c):
    """Merge two arrays and sort them"""

    count = 0
    merged_array = []

    b_ptr = 0
    c_ptr = 0

    while b_ptr < len(array_b) and c_ptr < len(array_c):

        if array_c[c_ptr] < array_b[b_ptr]:
            merged_array.append(array_c[c_ptr])
            c_ptr += 1
            count += len(array_b) - b_ptr
        else:
            merged_array.append(array_b[b_ptr])
            b_ptr += 1

    while b_ptr < len(array_b):
        merged_array.append(array_b[b_ptr])
        b_ptr += 1

    while c_ptr < len(array_c):
        merged_array.append(array_c[c_ptr])
        c_ptr += 1

    return (merged_array, count)


class TestSortAndCount(unittest.TestCase):

    def test_simple_case(self):
        sorted_array, count = sort_and_count([5, 4, 3, 2, 1])
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(count, 10)

    def test_simple_case_2(self):
        sorted_array, count = sort_and_count([2, 4, 1, 3, 5])
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(count, 3)


def test_file_input():
    """Check with the input file"""
    test_file = "/Users/Anirudh/coursera/problems/count_inversions_test.txt"
    contents = []

    with open(test_file, "r") as file:
        for line in file.readlines():
            contents.append(int(line.strip()))

    sorted_arr, count = sort_and_count(contents)

    with open("sorted_arr.txt", "w") as o_file:
        for num in sorted_arr:
            o_file.write(str(num) + "\n")

    print(count)


if __name__ == "__main__":
    test_file_input()
