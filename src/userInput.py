import os
from src.fileParser import FileParser
from src.soundex import Soundex

class UserInteraction:
    def __init__(self, initial_message):
        print("Hi, there!")

        self.message = initial_message
        self.path = ""
        self.word = ""

    def start_interaction(self):
        self.take_user_input()
        print("I'm on it!")
        file_parser = FileParser(self.path)
        file_parser.read_file()
        file_content = file_parser.file_content

        soundex = Soundex(file_content, self.word)
        soundex.soundex()
        print("-------------------------------")
        print("Your word was: " + self.word)
        print("Here are the top five matches according to yours truly:")
        for word in soundex.top_five_words:
            print(word)
        print("-------------------------------")
        print("Good-bye!")

    def take_user_input(self):
        is_file = False
        while not is_file:
            user_input = input(self.message)
            self.path, self.word = user_input.split(" ")
            is_file = self.verify_file()

    def verify_file(self):
        file, ext = os.path.splitext(self.path)
        word = self.word.strip()
        if os.path.isfile(self.path) and ext == '.txt' and word.isalpha():
            return True
        else:
            self.message = "Whops, your input is not valid, try again: "
            return False
