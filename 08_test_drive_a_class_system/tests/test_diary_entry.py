from lib.diary_entry import *

def test_init_function():
    diary_entry1 = DiaryEntry("My Title 1", "This is my diary entry 1.")
    result = diary_entry1._title
    assert result == "My Title 1"
    result = diary_entry1._contents
    assert result == "This is my diary entry 1."

def test_count_words_returns_contents_word_count():
    diary_entry1 = DiaryEntry("My Title 1", "This is my diary entry 1.")
    assert diary_entry1.count_words() == 6

def test_reading_time_returns_time_to_read_contents():
    diary_entry1 = DiaryEntry("My Title 1", "This is my diary entry 1.")
    assert diary_entry1.reading_time(3) == 2

def test_reading_times_return_zero_when_no_contents():
    diary_entry1 = DiaryEntry("My Title 1", "")
    assert diary_entry1.reading_time(3) == 0

def test_reading_chunk_called_once_returns_correct_chunk():
    diary_entry1 = DiaryEntry("My Title 1", "One Two Three Four Five Six Seven Eight Nine Ten")
    assert diary_entry1.reading_chunk(2,3) == "One Two Three Four Five Six"

def test_reading_chunk_called_twice_returns_correct_chunk():
    diary_entry1 = DiaryEntry("My Title 1", "One Two Three Four Five Six Seven Eight Nine Ten")
    diary_entry1.reading_chunk(2,3)
    assert diary_entry1.reading_chunk(2,3) == "Seven Eight Nine Ten"

def test_reading_chunk_wraps_back_around():
    diary_entry1 = DiaryEntry("My Title 1", "One Two Three Four Five Six Seven Eight Nine Ten")
    diary_entry1.reading_chunk(2,3) 
    diary_entry1.reading_chunk(2,3)    
    assert diary_entry1.reading_chunk(4,2) == "One Two Three Four Five Six Seven Eight"

def test_reading_chunk_returns_blank_when_no_entries():
    diary_entry1 = DiaryEntry("My Title 1", "")
    assert diary_entry1.reading_chunk(4,2) == ''