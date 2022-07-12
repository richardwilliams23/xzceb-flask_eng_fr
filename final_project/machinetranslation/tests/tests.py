"""
Module to test the functions in translator.py
"""
import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """ Tests for the english_to_french function. """

    def test_english_to_french(self):
        """ Tests for null and Hello to Bonjour """
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('House'), 'Maison')


class TestFrenchToEnglish(unittest.TestCase):
    """ Tests for the french_to_english function. """

    def test_french_to_english(self):
        """ Tests for null and Bonjour to Hello """
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Maison'), 'House')


if __name__ == '__main__':
    unittest.main()
