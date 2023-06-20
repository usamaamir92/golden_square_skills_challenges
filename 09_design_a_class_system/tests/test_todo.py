from lib.todo import *

def test_construct_todo():
    todo = Todo("Cleaning")
    assert todo.task == "Cleaning"
    assert todo.complete == False

def test_mark_complete():
    todo = Todo("Cleaning")
    todo.mark_complete()
    assert todo.complete == True