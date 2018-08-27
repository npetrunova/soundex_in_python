import threading


class ComparisonThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
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
    def compare_words(self,
                      input_word,
                      input_soundex_value,
                      word_from_text,
                      word_from_text_soundex):
        if word_from_text.lower() != input_word.lower():
            if word_from_text_soundex == input_soundex_value:
                    self.soundex_score = 8
            elif word_from_text_soundex[0] == input_soundex_value[0]:
                if word_from_text_soundex[1:2] == input_soundex_value[1:2]:
                    if word_from_text_soundex[2] != '0':
                        self.soundex_score = 7
                    else:
                        self.soundex_score = 2
            elif word_from_text_soundex[2:3] == input_soundex_value[2:3]:
                if word_from_text_soundex[2] != '0':
                    self.soundex_score = 6
            elif word_from_text_soundex[1] == input_soundex_value[1]:
                if word_from_text_soundex[3] == input_soundex_value[3]:
                    self.soundex_score = 5
                else:
                    self.soundex_score = 2
            elif word_from_text_soundex[2:3] == input_soundex_value[1:2]:
                    self.soundex_score = 4
            elif word_from_text_soundex[1:2] == input_soundex_value[2:3]:
                    self.soundex_score = 3
            elif word_from_text_soundex[2] == input_soundex_value[2]:
                    self.soundex_score = 1
            elif word_from_text_soundex[3] == input_soundex_value[3]:
                    self.soundex_score = 1


