"""
Algorithm to compute minimum number of edit operations that are needed to convert one string to
another. This is a classic dynamic programming problem.
"""
import unittest

def levenshtein_distance(original_str, edited_str) -> int:
    """
    original_str: The string before edit operations are performed.
    edited_str: The string after edit operations are performed

    returns the minimum number of edits required.

    O(N * M) time
    O(N * M) space
    """

    # initialize 2D array
    # +1 is for "" (empty strings) which is the base case
    num_edits = [
        [col for col in range(len(original_str) + 1)] for row in range(len(edited_str) + 1)
    ]

    # initialize columns (base case)
    for row in range(1, len(edited_str) + 1):
        num_edits[row][0] = 1 + num_edits[row - 1][0]

    # update cells
    for row in range(1, len(edited_str) + 1):
        for col in range(1, len(original_str) + 1):

            if edited_str[row - 1] == original_str[col - 1]:
                # chars are same then copy the previous value
                num_edits[row][col] = num_edits[row - 1][col - 1]
            else: 
                # use the formula
                num_edits_required_now = 1
                num_edits_so_far = min(
                        num_edits[row - 1][col],
                        num_edits[row][col - 1],
                        num_edits[row - 1][col - 1]
                    )
                num_edits[row][col] = num_edits_required_now + num_edits_so_far

    # return the last value
    # using bottom up dynamic programming
    return num_edits[-1][-1]
    
class TestLevenshteinDistance(unittest.TestCase):

    def test_1(self):
        orig = "ayd"
        edited = "abcd"

        self.assertEqual(levenshtein_distance(orig, edited), 2)
        
if __name__ == "__main__":
    unittest.main()
