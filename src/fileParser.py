import re

class FileParser:
    def __init__(self, path):
        self.path = path
        self.file_file_content_all_lower = []
        self.file_content = []

    def read_file(self):
        file = open(self.path, encoding="utf8")
        for line in file:
            self.split_to_list(line)

    def split_to_list(self, line):
        list_of_words = re.findall(r"[\w']+", line)
        for word in list_of_words:
            clean_word = re.sub(r'[^\w\s]', '', word)
            if len(clean_word) > 0 and word.isalpha():
                if clean_word.lower().strip() not in self.file_file_content_all_lower:
                    self.file_file_content_all_lower.append(clean_word.lower().strip())
                    self.file_content.append(clean_word.strip())


