import threading

class ComparisonThread(threading.Thread):
    def __init__(self, input_word, input_soundex_value, word_from_text, word_from_text_soundex):
        threading.Thread.__init__(self)
        self.input_word = input_word
        self.input_soundex_value = input_soundex_value
        self.word_from_text = word_from_text
        self.word_from_text_soundex = word_from_text_soundex
        self.soundex_score = 0

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
        if self.word_from_text.lower() != self.input_word.lower():
            if self.word_from_text_soundex == self.input_soundex_value:
                    self.soundex_score = 8
            elif self.word_from_text_soundex[0] == self.input_soundex_value[0]:
                if self.word_from_text_soundex[1:2] == self.input_soundex_value[1:2]:
                    if self.word_from_text_soundex[2] != '0':
                        self.soundex_score = 7
                    else:
                        self.soundex_score = 2
            elif self.word_from_text_soundex[2:3] == self.input_soundex_value[2:3]:
                if self.word_from_text_soundex[2] != '0':
                    self.soundex_score = 6
            elif self.word_from_text_soundex[1] == self.input_soundex_value[1]:
                if self.word_from_text_soundex[3] == self.input_soundex_value[3]:
                    self.soundex_score = 5
                else:
                    self.soundex_score = 2
            elif self.word_from_text_soundex[2:3] == self.input_soundex_value[1:2]:
                    self.soundex_score = 4
            elif self.word_from_text_soundex[1:2] == self.input_soundex_value[2:3]:
                    self.soundex_score = 3
            elif self.word_from_text_soundex[2] == self.input_soundex_value[2]:
                    self.soundex_score = 1
            elif self.word_from_text_soundex[3] == self.input_soundex_value[3]:
                    self.soundex_score = 1


