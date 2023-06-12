def make_snippet(string):
    word_list = string.split(' ')
    new_string = ''
    if len(word_list) < 6:
        return string
    else:
        for i in range(0,4):
            new_string += (word_list[i] + ' ')
        new_string += (word_list[4] + '...')
        return new_string