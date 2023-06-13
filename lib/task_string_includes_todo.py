def task_string_includes_todo(text) :
    if text == '' :
        raise Exception("No text entered.")
    if type(text) != str :
        raise Exception("Not a string") 
    if '#TODO' in text :
        return True
    else :
        return False
