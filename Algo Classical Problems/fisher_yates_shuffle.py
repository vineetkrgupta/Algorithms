"""
Fisher yates shuffle or Knuth's shuffle is an algorithm to shuffle a given sequence where the 
indexes are mathematically proven to be randomzid and equally weighted. 
"""
import random

def fisher_yates_shuffle(sequence):
    """Shuffles the sequence in-place randomly and returns it"""
    
    if len(sequence) < 1:
        return sequence

    index_last = len(sequence) - 1 

    for index_curr in range(index_last):
        index_random = random.randint(index_curr, index_last)

        if index_random != index_curr:
            sequence[index_curr], sequence[index_random] =\
                    sequence[index_random], sequence[index_curr]

    return sequence
