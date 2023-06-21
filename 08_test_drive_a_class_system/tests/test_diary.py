from lib.diary import *
from lib.diary_entry import *

def test_to_check_init_function():
    diary1 = Diary()
    result = diary1._entries_list
    assert result == []

def test_all_with_no_entries():
    diary1 = Diary()
    assert diary1.all() == []

def test_count_words_with_no_entries():
    diary = Diary()
    assert diary.count_words() == 0

def test_reading_time_with_no_entries():
    diary = Diary()
    assert diary.reading_time(15) == 0

def test_best_entry_for_reading_time_with_no_entries():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(15,10) == None