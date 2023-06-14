from lib.diary_entry import *
import pytest
"""
Given a title and contents, #format returns:
"My Title: These are the contents"
"""

def test_format_with_title_and_contents():
    diary_entry = DiaryEntry("My Title","These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

"""
Given a title and contents, #count_words returns:
The number of words in the contents.
"""

def test_count_words_with_title_and_contents():
    diary_entry = DiaryEntry("My Title","These are the contents")
    result = diary_entry.count_words()
    assert result == 4

"""
Given contents and a reading speed, #reading_time returns:
A float representing the number of minutes required to read
"""

def test_reading_time_with_contents_and_rpm():
    diary_entry = DiaryEntry("My Title","These are the contents")
    result = diary_entry.reading_time(20)
    assert result == 0.2

"""
Given contents, a reading speed and number of minutes the user has,
#reading_chunk returns a chunk of contents that the user could read.
"""

def test_reading_chunk_with_contents_rpm_and_minutes():
    diary_entry = DiaryEntry("My Title","These are the contents")
    result = diary_entry.reading_chunk(20, 0.1)
    assert result == "These are"

"""
Given contents, a reading speed and number of minutes the user has 
and calling #reading_chunk twice returns the chunk of contents the
user could read after the first #reading_chunk call.
"""

def test_reading_chunk_again():
    diary_entry = DiaryEntry("My Title","These are the contents")
    diary_entry.reading_chunk(20, 0.1)
    result = diary_entry.reading_chunk(20, 0.1)
    assert result == "the contents"

"""
Given contents, a reading speed and number of minutes the user has 
and calling #reading_chunk three times returns the first chunk of
contents.
"""

def test_reading_chunk_third_time():
    diary_entry = DiaryEntry("My Title","These are the contents")
    diary_entry.reading_chunk(20, 0.1)
    diary_entry.reading_chunk(20, 0.1)
    result = diary_entry.reading_chunk(20, 0.1)
    assert result == "These are"

# Given no title or contents should return error message - 'Need to enter title and contents'

def test_format_no_title_and_no_content() :
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry('','')
        diary_entry.format()
    error_message = str(e.value)
    assert error_message == 'Need to enter title and contents'
