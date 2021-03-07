"""
Given an array of numbers from 1..n, find the duplicate
"""

def get_duplicate_value(sequence):
    """
    O(n) - time
    O(n) - space
    """

    # keep track of visited numbers
    visited = set()

    for number in sequence:

        # if you encounter a number that has already been visited, then that's the repeated number
        if number in visited:
            return number
        else:
            visited.add(number)

    return None

def search_for_duplicated_value(sequence):
    """
    Using a varient of the binary search. Note that it does not return the first duplicate value 
    but one of the duplicate values.

    O(nlogn) - time
    O(1) - space
    """

    floor = 0
    ceiling = len(sequence) - 1

    while floor < ceiling:

        mid = floor + ((ceiling - floor) // 2)
        lower_floor, lower_ceiling = floor, mid
        higher_floor, higher_ceiling = mid + 1, ceiling

        # find the total number of numbers in lower range
        num_items_in_lower = 0
        for number in sequence:
            if lower_floor <= number <= lower_ceiling:
                num_items_in_lower += 1

        # find the total possible number in lower range
        distinct_possible_integers_in_lower = lower_ceiling - lower_floor + 1

        # based on this refine your search
        if num_items_in_lower > distinct_possible_integers_in_lower:
            floor, ceiling = lower_floor, lower_ceiling
        else:
            floor, ceiling = higher_floor, higher_ceiling

    return floor

def graph_search_duplicated_value(sequence):
    """
    A graph search for the duplicated value.

    O(n) - time
    O(1) - space
    """

    # 1. Get inside the cycle
    max_number = len(sequence) - 1
    pos_in_cycle = max_number + 1
    for _ in range(max_number):
        pos_in_cycle = sequence[pos_in_cycle - 1]

    # 2. Find the length of a cycle
    marker = pos_in_cycle
    curr_pos = sequence[pos_in_cycle - 1]
    cycle_len = 1

    while curr_pos != marker:
        curr_pos = sequence[curr_pos - 1]
        cycle_len += 1

    # 3. Find the first node of the cycle
    first_runner = max_number + 1
    second_runner = max_number + 1

    for _ in range(cycle_len):
        second_runner = sequence[second_runner - 1]

    while first_runner != second_runner:
        first_runner = sequence[first_runner - 1]
        second_runner = sequence[second_runner - 1]

    return first_runner
