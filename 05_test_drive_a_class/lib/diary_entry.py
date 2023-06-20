import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        read_up_to = 0
        self.read_up_to = read_up_to
        # Parameters:
        #   title: string
        #   contents: string

    def format(self):
        if self.title == '' or self.contents == '' :
            raise Exception('Need to enter title and contents')
        return f"{self.title}: {self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        return len(self.contents.split())
        # Returns:
        #   int: the number of words in the diary entry

    def reading_time(self, wpm):
        return len(self.contents.split())/wpm

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm*minutes
        words = self.contents.split()
        start_of_chunk = self.read_up_to
        end_of_chunk = int(self.read_up_to + number_of_words)
        self.read_up_to = end_of_chunk
        if self.read_up_to > len(self.contents.split()) :
            self.read_up_to = 0
            start_of_chunk = self.read_up_to
            end_of_chunk = int(self.read_up_to + number_of_words)
            chunk = words[start_of_chunk:end_of_chunk]
            return " ".join(chunk)
        else :
            chunk = words[start_of_chunk:end_of_chunk]
            self.read_up_to = end_of_chunk
            return " ".join(chunk)

    
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.