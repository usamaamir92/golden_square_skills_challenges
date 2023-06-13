from lib.task_string_includes_todo import *
import pytest

def test_task_string_doesnt_include_todo() :
    text = task_string_includes_todo('I need to clean the bedroom')
    assert text == False

def test_task_string_does_include_todo() :
    text = task_string_includes_todo('I need to clean the bedroom #TODO')
    assert text == True

def test_empty_string() :
    with pytest.raises(Exception) as e:
        task_string_includes_todo('')
    error_message = str(e.value)
    assert error_message == "No text entered."

def test_non_string() :
    with pytest.raises(Exception) as e:
        task_string_includes_todo(123)
    error_message = str(e.value)
    assert error_message == "Not a string"