from lib.grammar_stats import *
import pytest

def test_for_check():
    #Must have captial letter and full stop/?/!
    #one test for capital letter, another for punctuation mark
    new_test = GrammarStats()
    result = new_test.check("This is a string.")
    assert result == True

def test_for_check_failure():
    #Must have captial letter and full stop/?/!
    #one test for capital letter, another for punctuation mark
    new_test = GrammarStats()
    result = new_test.check("This is a string")
    assert result == False

#Create a variable that counts the total tests, and another variable
#to count the number of True and a third one for the number of False
#and return the overall percentage of True

def test_for_percentage_good():
    new_test = GrammarStats()
    new_test.check("This is a string.")
    new_test.check("This is a string")
    result = new_test.percentage_good()
    assert result == 50

def test_for_percentage_good_third():
    new_test = GrammarStats()
    new_test.check("This is a string.")
    new_test.check("This is a string")
    new_test.check("This is a string")
    result = new_test.percentage_good()
    assert result == 33.33

def test_for_empty_string():
    new_test = GrammarStats()
    with pytest.raises(Exception) as e:
        new_test.check("")
    error_message = str(e.value)
    assert error_message == "No text provided."

def test_for_non_string():
    new_test = GrammarStats()
    with pytest.raises(Exception) as e:
        new_test.check(123)
    error_message = str(e.value)
    assert error_message == "Not a string."

