import threading
from collections import OrderedDict


class ComparisonThread(threading.Thread):
    def __init__(self, word, soundex_value, dict_of_words):
        threading.Thread.__init__(self)
        self.word = word
        self.soundex_value = soundex_value
        self.dict_of_words = dict_of_words
        self.soundex_result = [word]
        self.soundex_score_from_top_four_matches = 0

# A quick note on the thought process behind it:
    # most score for exact match,
    # this means that there are some cases where for example 'a' and 'ah'\\
    # would be exact match, same for 'the' and 'two'\\
    # I decided to keep values like T000 or A000 as in some cases those\\
    # might mean meaningful words that genuinely sound the same like \\
    # 'sea' and 'see'. In order to ignore prepositions like 'the' and\\
    # 'a' it would be best to use a stop words remover method.\\
    # However, in cases like 'as' and 'an', I decided to ignore \\
    # the last two 00s and treat
    def compare_words(self):
        soundex_word_bucket = {}
        for key, value in self.dict_of_words.items():
            if key.lower() != self.word.lower():
                if value == self.soundex_value:
                    soundex_word_bucket[key] = 8
                elif value[0] == self.soundex_value[0]:
                    if value[1:2] == self.soundex_value[1:2]:
                        if value[2] != '0':
                            soundex_word_bucket[key] = 7
                        else:
                            soundex_word_bucket[key] = 2
                    elif value[2:3] == self.soundex_value[2:3]:
                        if value[2] != '0':
                            soundex_word_bucket[key] = 6
                    elif value[1] == self.soundex_value[1]:
                        if value[3] == self.soundex_value[3]:
                            soundex_word_bucket[key] = 5
                        else:
                            soundex_word_bucket[key] = 2
                    elif value[2:3] == self.soundex_value[1:2]:
                        soundex_word_bucket[key] = 4
                    elif value[1:2] == self.soundex_value[2:3]:
                        soundex_word_bucket[key] = 3
                    elif value[2] == self.soundex_value[2]:
                        soundex_word_bucket[key] = 1
                    elif value[3] == self.soundex_value[3]:
                        soundex_word_bucket[key] = 1

        soundex_dictionary = OrderedDict(sorted(soundex_word_bucket.items(), key=lambda x: x[1], reverse=True)[:4])
        for key, value in soundex_dictionary.items():
            self.soundex_result.append(key)

        self.soundex_score_from_top_four_matches = sum(soundex_dictionary.values())

