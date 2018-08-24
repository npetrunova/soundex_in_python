import os
from src.fileParser import FileParser
from src.soundex import Soundex

def main():
    print("Hi, there!")
    # user_input = "C:\\Users\\nikol.petrunova\Desktop\projects\python-task\wikiLT.txt lituania"
    user_input = input("Please give me a path and a word separated by space: ")
    path, word = user_input.split(" ")
    is_file = verify_file(path, word.strip())

    while not is_file:
        user_input = input("Whops, input is not valid, try again: ")
        path, word = user_input.split(" ")
        is_file = verify_file(path, word.strip())
    print("I'm on it!")
    file_parser = FileParser(path)
    file_parser.read_file()
    file_content = file_parser.file_content

    soundex = Soundex(file_content, word)
    soundex.soundex()
    print("-------------------------------")
    print("Your word was: " + word)
    print("Here are the top five matches according to yours truly:")
    for word in soundex.top_five_words:
        print(word)
    print("-------------------------------")
    print("Good-bye!")

def verify_file(path, word):
    file, ext = os.path.splitext(path)
    return os.path.isfile(path) and ext == '.txt' and word.isalpha()


main()
