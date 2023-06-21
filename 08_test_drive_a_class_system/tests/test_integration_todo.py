from lib.todo import *
from lib.todo_list import *

def test_todo_list_construct():
    todo_list = TodoList()
    assert todo_list.list_todos == []

def test_add_adds_to_list_of_todos():
    todo_list = TodoList()
    todo1 = Todo("Cleaning")
    todo_list.add(todo1)
    assert todo_list.list_todos == [todo1]

def test_incomplete_returns_all_incomplete_todos():
    todo_list = TodoList()
    todo1 = Todo("Cleaning")
    todo_list.add(todo1)
    todo2 = Todo("Shopping")
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1,todo2]

def test_complete_returns_all_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Cleaning")
    todo_list.add(todo1)
    todo2 = Todo("Shopping")
    todo2.mark_complete()
    todo_list.add(todo2)
    todo3 = Todo("Laundry")
    todo3.mark_complete()
    todo_list.add(todo3)
    assert todo_list.complete() == [todo2,todo3]

def test_give_up_marks_all_tasks_as_complete():
    todo_list = TodoList()
    todo1 = Todo("Cleaning")
    todo_list.add(todo1)
    todo2 = Todo("Shopping")
    todo_list.add(todo2)
    todo3 = Todo("Laundry")
    todo_list.add(todo3)
    todo_list.give_up()
    assert todo_list.complete() == [todo1,todo2,todo3]    
