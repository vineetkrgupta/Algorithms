"""
Notes:
    - Algorithm to check if a given string is a palindrome.
    - Simple & Elegant
"""

def is_palindrome(input_str):
    """Returns True if string is palindrome else False"""

    left_ptr = 0
    right_ptr = len(input_str) - 1

    while left_ptr < right_ptr:

        if input_str[left_ptr] != input_str[right_ptr]:
            return False

        left_ptr += 1
        right_ptr -= 1

    return True
