import unittest

from .name_function import *

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def setUp(self):

        self.input_name_first = "Janis"
        self.input_name_last = "Joplin"
        self.expected_result = "Janis Joplin"

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""

        formatted_name = get_formatted_name(self.input_name_first, self.input_name_last)

        self.assertEqual(formatted_name, self.expected_result)
