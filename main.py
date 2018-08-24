import os
from src.fileParser import FileParser
from src.soundex import Soundex

def main():
    print("Hi, there!")
    path = "C:\\Users\\nikol.petrunova\Desktop\projects\python-task\wikiLT.txt"
    # path = input("Where is the file you want me to play with? ")
    is_file = verify_file(path)

    while not is_file:
        path = input("Whops, this is is not a valid path, try again: ")
        is_file = verify_file(path)

    file_parser = FileParser(path)
    file_parser.read_file()
    file_content = file_parser.file_content

    soundex = Soundex(file_content)
    soundex.soundex()
    for word in soundex.topFiveWords:
        print(word)


def verify_file(path):
    file, ext = os.path.splitext(path)
    return os.path.isfile(path) and ext == '.txt'


main()
