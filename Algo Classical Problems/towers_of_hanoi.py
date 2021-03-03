"""
Classic problem of recursion
"""

def towers_of_hanoi(tower_a, tower_b, tower_temp, num_discs):

    if num_discs == 1:
        tower_b.append(tower_a.pop())
    else:
        towers_of_hanoi(tower_a, tower_temp, tower_b, num_discs - 1)
        towers_of_hanoi(tower_a, tower_b, tower_temp, 1)
        towers_of_hanoi(tower_temp, tower_b, tower_a, num_discs - 1)

