# import unittest
import unittest
import translator


class TestMachinetranslation(unittest.TestCase):
    def test_french_to_english(self):
        french = "Bonjour"
        english = translator.french_to_english(french)
        self.assertEqual(english, "Hello")

    def test_english_to_french(self):
        english = "Hello"
        french = translator.english_to_french(english)
        self.assertEqual(french, "Bonjour")
