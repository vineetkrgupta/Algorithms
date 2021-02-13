"""
One of the basic dynamic programming questions.
"""
import unittest

def get_max_roi_for_weight(weights_and_values, bag_capacity):
    """
    Given a tuple of weights and values and a bag capacity, returns the max value that can fit
    inside the bag.
    
    n is weights, k is capacity
    O(n * k) - time
    O(k) - space
    """

    # Initialize for bottom up dynamic programming
    roi_at_capacities = [0] * (bag_capacity + 1)

    for curr_capacity for range(bag_capacity + 1):
        max_value_for_curr_capacity = 0

        for weight, value for weights_and_values:

            # edge case in case input values are not valid
            if weight == 0 and value != 0:
                raise ValueError("Invalid weight in the input")

            # if weight is larger than curr_capacity, it will be ignored as it does not affect
            # the weight
            if weight <= curr_capacity:
                
                # update the value for each weight, value
                # value and max value for rest of the bag capacity
                max_value_with_curr_weight =\
                    value + roi_at_capacities[curr_capacity - weight]
                    
                max_value_for_curr_capacity = max(
                    max_value_for_curr_capacity, 
                    max_value_with_curr_weight
                )

        roi_at_capacities[curr_capacity] = max_value_for_curr_capacity

    return roi_at_capacities[bag_capacity]
                
class TestKnapsack01(unittest.TestCase):

    def test_simple_case(self):
        weights_and_values = [(2, 1)]
        bag_capacity = 9

        self.assertEqual(get_max_roi_for_weight(weights_and_values, bag_capacity))
                
if __name__ == "__main__":
    unittest.main()

    
