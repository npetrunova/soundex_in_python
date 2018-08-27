from src.userInput import UserInteraction
import unittest2


class UserInterractionTest(unittest2.TestCase):

        def test_veryfy_input_correct(self):
            self.userInterraction = UserInteraction("")
            self.userInterraction.path = "C:\\Users\\nikol.petrunova\Documents\GitHub\soundex_in_python\wikiLT.txt"
            self.userInterraction.word = "lituania"

            result = self.userInterraction.verify_file()
            self.assertEqual(result, True)

        def test_veryfy_input_incorrect_path(self):
            self.userInterraction = UserInteraction("")
            self.userInterraction.path = ""
            self.userInterraction.word = "lituania"

            result = self.userInterraction.verify_file()
            self.assertEqual(result, False)

        def test_veryfy_input_incorrect_word(self):
            self.userInterraction = UserInteraction("")
            self.userInterraction.path = "C:\\Users\\nikol.petrunova\Documents\GitHub\soundex_in_python\wikiLT.txt"
            self.userInterraction.word = " "

            result = self.userInterraction.verify_file()
            self.assertEqual(result, False)


if __name__ == '__main__':
    unittest2.main()

