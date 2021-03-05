"""
Notes:
    - Created by David Hoffman.
    - Lossless compression of data.
    - Uses a varaible length code that depends on frequency of characters.
    - High frequency chars use smallest codes & least fequently used chars use largest codes.
    - Create a huffman tree and traverse to find codes.
    - O(nlogn) for encoding each char
    - Huffman encoding prevents ambiguity by using prefix code.


Applications:
    - Computer Networks as data can be compressed.

References:
    - https://www.programiz.com/dsa/huffman-coding
"""
import unittest

def encode(str):
    """Encode the given string using huffman encoding algorithm
    1. Calculate frequency of each char.
    2. Sort characters based on frequency and store it in a Priority Queue.
    3. Make each unique char as a leaf node.
    4. Create an empty node z. Assign min freq to left of z, and second min to right of z. 
    5. Set value of z as sum of the two freq.
    6. Remove these two min frequencies from Q and add the sum into the frequencies.
    7. Insert z into the tree.
    8. Repeat for all characters.
    9. For each non-leaf node. Assign 0 to left and 1 to right.
    10. Send the tree as well as compressed string.
    """
    # Create a priority queue consisting of each unique char
    # Sort in the ascending order of frequency
    # for all unique characters
    #   create a new node
    #   extract minimum value from queue and assign it to the left
    #   extract minimum value from queue and assign it to the right
    #   calculate the sum (left + right) and assign it as value to the node
    #   insert the node into the tree
    pass

def decode(str, tree):
    """Decode the received string using huffman encoding algorithm"""
    pass

class TestHuffmanEncoding(unittest.TestCase):

    def simple_test_case(self):
        """TODO: Calculate the bytes used"""
        input_str = "Hello World"

if __name__ == "__main__":
    unittest.main()
