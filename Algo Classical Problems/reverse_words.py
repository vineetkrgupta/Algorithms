"""
Reversing a string
"""
import unittest

def reverse_string(chars, left=None, right=None):

    left = left if left is not None else 0
    right = right if right is not None else len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return chars

def reverse_words(sentence):

    # first reverse the whole sentence
    reverse_string(sentence)

    # reverse each word
    curr_word_start = 0
    for i in range(len(sentence) + 1):

        if i == len(sentence) or sentence[i] == " ":
            reverse_string(sentence, curr_word_start, i - 1)
            curr_word_start = i + 1

    return sentence

class TestReverseString(unittest.TestCase):

    def test_reverse_string_with_odd_length(self):
        self.assertEqual(
            reverse_string(list("abc")),
            list("cba")
        )

    def test_reverse_string_with_even_length(self):
        self.assertEqual(
            reverse_string(list("anirud")),
            list("durina")
        )

    def test_reverse_words(self):
        self.assertEqual(
            reverse_words(list("I am Batman")),
            list("Batman am I")
        )
            
if __name__ == "__main__":
    unittest.main()
    


