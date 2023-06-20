from lib.count_words import *

def test_no_words_returns_zero():
    assert count_words("") == 0

def test_three_space_separated_words():
    assert count_words("horse dog cat") == 3

def test_five_comma_separated_words():
    assert count_words("use,five,different,words,please") == 5