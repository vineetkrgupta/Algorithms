"""
Algorithm to find the permutations
"""
import unittest

def get_permutations_1(sequence, permutation_curr = [], permutations = []):
    """
    Returns all the possible permutations of the given sequence

    O(n^2 * n!) time
    O(n * n!) space
    """

    # base case, when sequence is empty current permutation is the only one possible
    if not len(sequence) and len(permutation_curr):
        permutations.append(permutation_curr)
        return

    for index_curr in range(len(sequence)):

        sequence_without_current_element = sequence[:index_curr] + sequence[index_curr + 1:]
        permutation_with_current_element = permutation_curr + [sequence[index_curr]]

        get_permutations_1(
            sequence_without_current_element, 
            permutation_with_current_element, 
            permutations
        )
    
    return permutations

def get_permutations_2(string_given):

    # base case
    if len(string_given) <= 1:
        return set([string_given])

    string_without_last_character = string_given[:-1]
    last_character = string_given[-1]

    all_permutations_without_last_character = get_permutations_2(string_without_last_character)

    permutations = set()
    for permutation_curr in all_permutations_without_last_character:
        for position in range(len(permutation_curr) + 1):
            
            permutation_new = (
                permutation_curr[:position] + 
                last_character + 
                permutation_curr[position:]
            )

            permutations.add(permutation_new)

    return permutations

class TestPermutations(unittest.TestCase):

    def test_1(self):
        perms = get_permutations_2("flour")
        for perm in perms:
            print(perm)
        

if __name__ == "__main__":
    unittest.main()
