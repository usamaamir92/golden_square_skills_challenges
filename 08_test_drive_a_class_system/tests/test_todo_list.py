from lib.todo_list import *

def test_todo_list_construct():
    todolist1 = TodoList()
    assert todolist1.list_todos == []

def test_incomplete_when_no_todos():
    todolist1 = TodoList()
    assert todolist1.incomplete() == []

def test_complete_when_no_todos():
    todolist1 = TodoList()
    assert todolist1.complete() == []