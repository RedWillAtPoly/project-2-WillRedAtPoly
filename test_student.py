import unittest

from p2 import (
    score_guess,
    is_valid_guess,
    choose_secret,
    play_turn,
    WORDS
)

class TestScoreGuess(unittest.TestCase):
    #My unittest for score_guess
    def test_close_guess(self):
        self.assertEqual(score_guess('train','brain'), 'XYYYY')

    #My unittest for test_valid_guess
    def test_new_characters(self):
        self.assertFalse(is_valid_guess('?#*^&'))

    #my unittest for choosing first element for secret word
    def second_test_choose_word(self):
        word_list = ['adieu', 'audio','brain','skull']
        self.assertEqual(choose_secret(word_list), 'adieu')

    #my unittest for play_turn
    def test_semivalid_guess(self):
        self.assertEqual(play_turn('crane','brain'), 'XYYXO')

if __name__ == '__main__':
    unittest.main()