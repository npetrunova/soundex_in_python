import re
from src.comparisonThread import ComparisonThread
from collections import OrderedDict

class Soundex:
    def __init__(self, file_content, word):
        self.file_content = file_content
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
        self.soundex_dictionary = {}
        self.top_five_words = []
        self.word = word
        self.soundex_of_word = ''

    def soundex(self):
        self.soundex_of_word = self.convert_to_soundex(self.word)
        for word in self.file_content:
            soundex_word = self.convert_to_soundex(word)
            self.soundex_dictionary[word] = soundex_word

        self.soundex_compare()

    def convert_to_soundex(self, word):
        first_letter = word[0]
        remaining_word = word[1:]

        for key, value in self.patterns.items():
            remaining_word = self.replace_characters(remaining_word, key, value)

        if len(remaining_word) < 3:
            remaining_word += '0' * (3 - len(remaining_word))
        else:
            remaining_word = remaining_word[:3]

        return first_letter.upper() + remaining_word

    def replace_characters(self, word, pattern, new_character):
        return re.sub(pattern, new_character, word, flags=re.I)

    def soundex_compare(self):
        soundex_dictionary = {}
        for key, value in self.soundex_dictionary.items():
            comparison_thread = ComparisonThread(self.word, self.soundex_of_word, key, value)
            comparison_thread.start()
            comparison_thread.compare_words()
            score = comparison_thread.soundex_score
            soundex_dictionary[key] = score
        top_five_words_dict = OrderedDict(sorted(soundex_dictionary.items(),
                                          key=lambda x: x[1], reverse=True)[:5])

        self.top_five_words = list(top_five_words_dict.keys())

