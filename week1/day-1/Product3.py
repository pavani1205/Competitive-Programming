import unittest
import sys


def highest_product_of_3(list_of_ints):
    if(len(list_of_ints)<3):
        raise ValueError('Less than 3 items!')
    # Calculate the highest product of three numbers
    min1=min2=sys.maxsize
    max1=max2=max3=-sys.maxsize - 1
    for i in list_of_ints:
        if(i<=min1):
           min2=min1
           min1=i
        elif(i<=min2):
            min2=i
        if(i>=max1):
            max3=max2
            max2=max1
            max1=i
        elif(i>=max2):
            max3=max2
            max2=i
        elif(i>=max3):
            max3=i
            
        
    x=max(min1*min2*max1,max1*max2*max3)
    return x


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)