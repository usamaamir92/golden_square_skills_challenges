from lib.estimate_reading_time import *
import pytest


#Given a text string with 200 words
#the function returns 1.0

def test_with_200_words():
    text = 200*"words "
    result = estimate_reading_time(text)
    assert result == 1.0

#Given a text string with 300 words
#the function returns 1.5

def test_with_300_words():
    text = 300*"words "
    result = estimate_reading_time(text)
    assert result == 1.5

    #Given a text string with 400 words
#the function returns 2.0

def test_with_400_words():
    text = 400*"words "
    result = estimate_reading_time(text)
    assert result == 2.0

    #Given empty string the function returns an error message

def test_with_no_words():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for empty text."