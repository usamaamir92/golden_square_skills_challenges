from lib.diary import *
from lib.diary_entry import *
from lib.todo import *
from lib.todo_list import *

def test_add_diary_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary.add(diary_entry1)
    assert diary.diary_entries == [diary_entry1]

def test_all_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1,diary_entry2]

def test_get_readable_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. It is longer than entry 1.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.get_readable_entry(2,4) == [diary_entry1]


def test_get_readable_entry_multiple_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. It is longer than entry 1.")
    diary_entry3 = DiaryEntry("02/01/2023","This is my diary entry 3.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.get_readable_entry(2,4) == [diary_entry1,diary_entry3]

def test_no_readable_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. It is longer than entry 1.")
    diary_entry3 = DiaryEntry("02/01/2023","This is my diary entry 3.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.get_readable_entry(1,1) == None

def test_find_diary_entry_by_date():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. It is longer than entry 1.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.diary_entry_by_date("02/01/2023") == diary_entry2

def test_list_of_phone_numbers():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1. 07123456789, 0712458")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. 02984484920, 02035678900")
    diary_entry3 = DiaryEntry("02/01/2023","This is my diary entry 3.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.get_phone_numbers() == ["07123456789", "02984484920", "02035678900"]

def test_no_phone_numbers():
    diary = Diary()
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1. 0712789, 0712458")
    diary_entry2 = DiaryEntry("02/01/2023","This is my diary entry 2. 02984920, 020800")
    diary_entry3 = DiaryEntry("02/01/2023","This is my diary entry 3.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.get_phone_numbers() == None

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