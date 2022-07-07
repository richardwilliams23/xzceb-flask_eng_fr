"""
Python Project for AI course, Final assignment.
Module to test the functions in translator.py
"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ Tests for the english_to_french function. """
    def test_english_to_french(self):
        """ Test for null and one other """
        self.assertNotEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    """ Tests for the french_to_english function. """
    def test_french_to_english(self):
        """ Test for null and one other """
        self.assertNotEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
