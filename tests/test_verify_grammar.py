from lib.verify_grammar import *
import pytest

def test_capital_letter_and_period():
    text = verify_grammar("Hello my name is Usama.")
    assert text == True

def test_capital_letter_and_exclamation():
    text = verify_grammar("Hello my name is Usama!")
    assert text == True

def test_capital_letter_and_question():
    text = verify_grammar("Hello my name is Usama?")
    assert text == True

def test_capital_letter_and_no_punctuation():
    text = verify_grammar("Hello my name is Usama")
    assert text == False

def test_no_capital_with_punctuation():
    text = verify_grammar("hello my name is Usama.")
    assert text == False

def test_error_message():
    with pytest.raises(Exception) as e:
        verify_grammar("")
    error_message = str(e.value)
    assert error_message == "No text entered."
