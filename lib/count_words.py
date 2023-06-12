import re

def count_words(string):
    if len(string) == 0:
        return 0
    else:
        word_list = re.split(r',| ',string)
        return len(word_list)
