import re
from src.comparisonThread import ComparisonThread

class Soundex:
    def __init__(self, file_content):
        self.fileContent = file_content
        self.patterns = {
            '[aeiouy]': '',
            '[hw]': '',
            '[bfpv]+': '1',
            '[cgjkqsxz]+': '2',
            '[dt]+': '3',
            'l+': '4',
            '[mn]+': '5',
            'r+': '6'
        }
        self.soundexDictionary = {}
        self.topFiveWords = []
        self.soundex_top_score = 0

    def soundex(self):
        for word in self.fileContent:
            self.convert_word(word)

        self.soundex_compare()

    def convert_word(self, word):
        first_letter = word[0]
        remaining_word = word[1:]

        for key, value in self.patterns.items():
            remaining_word = self.replace_characters(remaining_word, key, value)

        if len(remaining_word) < 3:
            remaining_word += '0' * (3 - len(remaining_word))
        else:
            remaining_word = remaining_word[:3]

        soundex_word = first_letter.upper() + remaining_word
        self.soundexDictionary[word] = soundex_word

    def replace_characters(self, word, pattern, new_character):
        return re.sub(pattern, new_character, word, flags=re.I)

    def soundex_compare(self):
        for key, value in self.soundexDictionary.items():
            comparison_thread = ComparisonThread(key, value, self.soundexDictionary)
            comparison_thread.start()
            comparison_thread.compare_words()
            comparison_score = comparison_thread.soundex_score_from_top_four_matches
            if comparison_score > self.soundex_top_score:
                self.soundex_top_score = comparison_score
                self.topFiveWords = comparison_thread.soundex_result

