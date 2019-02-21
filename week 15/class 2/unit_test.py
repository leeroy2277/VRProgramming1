import unittest

from .password_functions import *

class Test_PW_Functions(unittest.TestCase):

    def test_pw_not_long_enough(self):

        sample_pass = "abcd"
        expected_result = False

        result = validate_password_length(sample_pass)

        self.assertEqual(expected_result, result)

    def test_pw_just_long_enough(self):
        sample_pass = "abcdabcd"
        expected_result = True

        result = validate_password_length(sample_pass)

        self.assertEqual(expected_result, result)

    def test_pw_long_enough(self):
        sample_pass = "abcdabcdx"
        expected_result = True

        result = validate_password_length(sample_pass)

        self.assertEqual(expected_result, result)