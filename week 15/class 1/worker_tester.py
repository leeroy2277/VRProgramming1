import unittest

from .Worker import *

class test_worker(unittest.TestCase):

    def setUp(self):

        number1 = 2
        number2 = 3
        self.adding_machine_instance = AddingMachine(number1, number2)


    def test_get_hourly_rate(self):

        expected = ' '

        result = self.get_hourly_rate.add()

        self.assertEqual(expected, result)

