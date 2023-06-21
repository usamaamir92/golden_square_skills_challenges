# File: lib/diary.py
from lib.diary_entry import *
class Diary:
    def __init__(self):
        self._entries_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._entries_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry 
        return self._entries_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total = 0
        for entry_list in self._entries_list:
            total += entry_list.count_words()
        
        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total = 0
        for entry_list in self._entries_list:
            total += entry_list.reading_time(wpm)
        
        return total

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_able_read = wpm * minutes
        title    = ''
        contents = ''
        word_count = 0
        for entry_list in self._entries_list:
            if entry_list.count_words() <= words_able_read and entry_list.count_words() > word_count:
                title    = entry_list._title
                contents = entry_list._contents
                word_count = entry_list.count_words()
        if word_count > 0:
            return DiaryEntry(title,contents)


