"""
Kadane's algorithm is the efficient algorithm to solve maximum subarray problem
"""
def kadane_algorithm(sequence: List[int]):
    """
    Greedy algorithm to track max sum 

    O(n) time 
    O(1) space
    """

    if len(sequence) < 1:
        return 0

    max_sum = sequence[0]
    curr_sum = sequence[0]

    for curr_index in range(1, len(sequence)):
        curr_sum = max(sequence[curr_index], curr_sum + sequence[curr_index])
        max_sum = max(curr_sum, max_sum)

    return max_sum

