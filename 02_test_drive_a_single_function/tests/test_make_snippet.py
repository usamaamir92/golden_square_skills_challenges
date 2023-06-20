from lib.make_snippet import *

def test_no_words_returns_blank():
    assert make_snippet('') == ''

def test_five_words_returns_correctly():
    assert make_snippet('Horse Goat Duck Dog Cat') == 'Horse Goat Duck Dog Cat'

def test_more_than_five_words_returns_correctly():
    assert make_snippet('Horse Goat Duck Dog Cat Chicken') == 'Horse Goat Duck Dog Cat...'

def test_three_words_returns_correctly():
    assert make_snippet('Horse Goat Duck') == 'Horse Goat Duck'