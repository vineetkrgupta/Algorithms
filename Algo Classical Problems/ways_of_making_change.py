"""Algorithm demonstrating the power of dynamic programming: It is simple and elegant and one of
the most important concepts in computer science."""

import unittest
from typing import List

def num_ways_of_making_change(amount: int, coins: List[int]):
    """Here amount represents the desired monetary value and coins is the denominations"""

    # Our approach uses bottom-up dynamic programming
    # i.e we first calculate what is needed for the lowest value first and build
    # the higher values as we go along
    
    # Initialize the data structure we will use to store all possible amounts 
    # we initialize all amounts to 0 first
    # we add 1 because our base case is making 0 amount
    num_ways = [0] * (amount + 1)

    # there is only one way to make 0 change, this is our base case
    # TODO: Figure out why this is?
    num_ways[0] = 1

    for coin in coins:

        # We loop from making the lowest possible value to the required value
        # amount + 1 since we want the for loop to run until amount
        for net_amount in range(1, amount + 1):
            if coin <= net_amount:
                num_ways[net_amount] += num_ways[net_amount - coin]

        print(num_ways)

    return num_ways[amount]

class TestMakingChange(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            num_ways_of_making_change(4, [1, 2]),
            3
        )

if __name__ == "__main__":
    unittest.main()
    
