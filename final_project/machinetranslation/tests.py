"""
Python Project for AI course, Final assignment.
Module to test the functions in translator.py
"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ Tests for the english_to_french function. """
    def test_english_to_french(self):
        """ Tests for null and Hello to Bonjour """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')




if __name__ == '__main__':
    unittest.main()
