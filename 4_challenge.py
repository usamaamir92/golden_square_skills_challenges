def get_most_common_letter(text):
    counter = {}
    new_text = text.replace(' ', '')
    for char in new_text:
        counter[char] = counter.get(char, 0) + 1
    # print('counter.items',list(counter.items()))
    # counter.items = [('t', 3), ('h', 3), ('e', 4), (' ', 8), ('r', 4), ('o', 7), ('f', 4), (',', 2), ('i', 2), ('s', 1), ('n', 1), ('!', 1)]
    letter = sorted(list(counter.items()), key=lambda item: item[1], reverse = True)[0]
    most_common_letter = list(letter.items())[0]
    print(letter)
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")