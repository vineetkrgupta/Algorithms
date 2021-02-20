"""
Merge sort is an important sorting algorithm which works by repeatedy diving the input
and merging them again after sorting the smaller sequences.

Runtime: O(nlogn)

TODO: 
1. In place sorting version
2. Iterative version
"""

def merge(seq1, seq2):
    """Merge two sorted arrays into a single array"""

    if not seq1 or not seq2:
        raise ValueError("Input sequences do not exist or empty")
    
    merged_size = len(seq1) + len(seq2)
    merged_seq = [None] * merged_size

    seq1_index = 0
    seq2_index = 0
    merged_index = 0

    while merged_index < merged_size:

        is_first_seq_exhausted = seq1_index >= len(seq1)
        is_second_seq_exhausted = seq2_index >= len(seq2)

        if (not is_first_seq_exhausted) and (
                is_second_seq_exhausted or seq1[seq1_index] <= seq2[seq2_index]
            ):
            merged_seq[merged_index] = seq1[seq1_index]
            seq1_index += 1
            merged_index += 1
        else:
            merged_seq[merged_index] = seq2[seq2_index]
            seq2_index += 1
            merged_index += 1

    return merged_seq

def merge_sort(seq):
    """Sort the input sequence using merge sort algorithm"""

    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]

    sorted_seq_left = merge_sort(left)
    sorted_seq_right = merge_sort(right)
    
    return merge(sorted_seq_left, sorted_seq_right)

