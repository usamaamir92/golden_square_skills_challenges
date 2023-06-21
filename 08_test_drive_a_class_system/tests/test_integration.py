from lib.diary import *
from lib.diary_entry import *

#Test to check that the add function adds to the list of diary entries.

def test_check_add_function_adds_to_list():
    diary1 = Diary()
    diary_entry1 = DiaryEntry("My Title 1","This is my diary entry 1.")
    diary1.add(diary_entry1)
    result = diary1._entries_list
    assert result == [diary_entry1]

#Test to check that the all function returns the list of diary entries.

def test_to_check_all_function():
    diary1 = Diary()
    diary_entry1 = DiaryEntry("My Title 1","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("My Title 2","This is my diary entry 2.")
    diary1.add(diary_entry1)
    diary1.add(diary_entry2)
    result = diary1.all()
    assert result == [diary_entry1,diary_entry2]


def test_check_count_words_function_with_multiple_entries():
    diary1 = Diary()
    diary_entry1 = DiaryEntry("My Title 1","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("My Title 2","This is my diary entry 2.")
    diary1.add(diary_entry1)
    diary1.add(diary_entry2)
    assert diary1.count_words() == 12

def test_reading_time_function_with_multiple_entries():
    diary1 = Diary()
    diary_entry1 = DiaryEntry("My Title 1","This is my diary entry 1.")
    diary_entry2 = DiaryEntry("My Title 2","This is my diary entry 2.")
    diary1.add(diary_entry1)
    diary1.add(diary_entry2)
    assert diary1.reading_time(3) == 4

def test_find_best_entry_for_reading_time():
    diary1 = Diary()
    diary_entry1 = DiaryEntry("My Title 1","This is my diary entry 1 One")
    diary_entry2 = DiaryEntry("My Title 2","This is my diary entry 2")
    diary_entry3 = DiaryEntry("My Title 3","This is my diary entry 2 One two")
    diary_entry4 = DiaryEntry("My Title 4","This is my diary entry 4")
    diary1.add(diary_entry1)
    diary1.add(diary_entry2)
    diary1.add(diary_entry3)
    diary1.add(diary_entry4)
    assert diary1.find_best_entry_for_reading_time(3,3)._title == "My Title 3"
    assert diary1.find_best_entry_for_reading_time(3,3)._contents == "This is my diary entry 2 One two"

