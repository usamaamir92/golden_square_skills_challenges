def verify_grammar(text):
    if text == "":
        raise Exception("No text entered.")
    suitable_punctuation = [".","!","?"]
    words_list = text.split()
    if words_list[0][0].isupper() and text[-1] in suitable_punctuation:
        return True
    else:
        return False