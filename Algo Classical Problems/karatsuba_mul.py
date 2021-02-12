"""
Karatsuba multiplication is a recursive algorithm to multiply two numbers

Only works for even number of digits that can be equally divided such as
1234 * 5678

TODO: 
    1. What if the numbers are not of same length?
    2. What if you want to multiply floating point numbers?
"""
import unittest

def get_number_of_digits(num):
    """Returns the number of digits in the number, assuming base 10"""

    curr_num = num
    count = 0
    while curr_num:
        curr_num = curr_num // 10
        count += 1

    return count

def arr_to_num(array):
    """Convert array of numbers to the number"""
    num = 0
    for (index, digit) in enumerate(array):
        num += digit * pow(10, index)
    return num

def split_into_two(num):
    """Splits the number into two and returns num digits"""

    curr_num = num
    num_array = []
    while curr_num:
        curr_num, remainder = divmod(curr_num, 10)
        num_array.append(remainder)

    num_digits = len(num_array)
    part_b = arr_to_num(num_array[:num_digits//2])
    part_a = arr_to_num(num_array[num_digits//2:])
    
    return (num_digits, part_a, part_b)


def karatsuba_mul(num_1, num_2):
    """Computes the multiplication of the input numbers"""
    
    if num_1 <= 9999 or num_2 <= 9999:
        return num_1 * num_2

    num_1_digits, num_a, num_b = split_into_two(num_1)
    num_2_digits, num_c, num_d = split_into_two(num_2)

    print(num_a, num_b, num_c, num_d)
    
    num_ac = karatsuba_mul(num_a, num_c)
    num_bd = karatsuba_mul(num_b, num_d)
    num_ab_cd = karatsuba_mul(num_a + num_b, num_c + num_d) - num_ac - num_bd

    part_1 = num_ac * pow(10, num_1_digits if num_1_digits % 2 == 0 
            else num_1_digits - 1)
    part_2 = num_bd
    part_3 = num_ab_cd * pow(10, num_1_digits // 2)
    
    print(part_1, part_2, part_3)

    return part_1 + part_2 + part_3
    
class TestKaratsubaMultiplication(unittest.TestCase):
    @unittest.skip("")
    def test_4_digit(self):
        answer = karatsuba_mul(1234, 5678)
        self.assertEqual(answer, 1234 * 5678)

    @unittest.skip("")
    def test_5_digit(self):
        answer = karatsuba_mul(12345, 67891)
        self.assertEqual(answer, 12345 * 67891)

    @unittest.skip("")
    def test_6_digit(self):
        answer = karatsuba_mul(123456, 654321)
        self.assertEqual(answer, 123456 * 654321)

    @unittest.skip("")
    def test_7_digit(self):
        answer = karatsuba_mul(1234567, 7654321)
        self.assertEqual(answer, 1234567 * 7654321)

    @unittest.skip("")
    def test_8_digit(self):
        answer = karatsuba_mul(12345678, 87654321)
        self.assertEqual(answer, 12345678 * 87654321)

    def test_9_digit(self):
        answer = karatsuba_mul(123456789, 123456789)
        self.assertEqual(answer, 123456789 * 987654321)

    @unittest.skip("")
    def test_10_digit(self):
        answer = karatsuba_mul(1234567891, 1234567891)
        self.assertEqual(answer, 1234567891 * 1234567891)


if __name__ == "__main__":
    unittest.main()
