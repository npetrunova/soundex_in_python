from src.soundex import Soundex
from src.comparisonThread import ComparisonThread
import unittest2


class SoundexTest(unittest2.TestCase):

    def test_convert_word_to_soundex(self):
        soundex = Soundex([], "")
        result = soundex.convert_to_soundex("Lithuania")
        self.assertEqual(result, "L350")

    def test_replace_character(self):
        soundex = Soundex([], "")
        result = soundex.replace_characters("dissolution", '[cgjkqsxz]+', '2')
        self.assertEqual(result, 'di2olution')

    def test_compare_soundex(self):
        comparisonThread = ComparisonThread()
        comparisonThread.start()
        comparisonThread.compare_words("Lithuania", "L350", "lituania", "L350")
        result = comparisonThread.soundex_score
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest2.main()

