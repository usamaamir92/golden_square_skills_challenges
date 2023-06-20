from lib.diary_entry import *

def test_init_function():
    diary_entry1 = DiaryEntry("01/01/2023","This is my diary entry 1.")
    assert diary_entry1.date == "01/01/2023"
    assert diary_entry1.text == "This is my diary entry 1."