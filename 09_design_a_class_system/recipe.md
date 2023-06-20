Describe the problem:

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


Design the class system: 

Diary
 - diary entries
 - add(diary_entry)
 - all_diary_entries()
    => [diary_entries...]
 - get_diary_entry_for_reading_speed_and_time(Minutes, WPM)
    => diary_entry
 - get_all_phone_number()
    => [phone_numbers...]
 - find_diary_entry_by_date(date)
    => diary_entry
______________________________________
|
| owns a list of
|
______________________________________
Diary entry
 - date
 - text 
_______________________________________


Todo list
- list_todos
- add()
- incomplete()
- complete()
_______________________________________
|
| owns a list of
|
________________
Todo
- task
- mark_as_complete()

class Diary:
    #User_facing properties:
    #    diary_entries: list of instances of DiaryEntry

    def __init__(self):
        pass

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of DiaryEntry
        # Side -effects:
        #   adds the diary_entry to the diary_entries property of the self object
        pass

    def all_diary_entries(self):
        # Returns:
        #   A list of all the diary_entry objects in the diary_entries property
        pass
    
    def get_readable entry(self, WPM, Minutes)
        # Parameters: 
        #   WPM: int
        #   Minutes: int
        # Returns:
        #   The diary entry objects that have the text property that has the closest number of words to the WPM * Minutes
        
    def get_all_phone_number()
       # Returns:
       # A list of phone number objects

    def find_diary_entry_by_date(date)
       # Parameters:
       # date: datetime
       # Returns:
       # The diary entry object for the given date


class DiaryEntry:
       # def __init__(self, date, text)
       # constructor function with date and entry text as arguments


class ToDoList:
       # def __init__(self,list_todos)
       # constructor function with list of todos as public property

       # def add(todo)
       # function that adds instance of todo to list_todos

       # def incomplete()
       # Returns:
       # A list of Todo instances representing the todos that are not complete

       # def complete()
       # Returns:
       # A list of Todo instances representing the todos that are complete

class ToDo:
       # def __init__(self,task,complete)
       # constructor function with task and complete/incomplete as arguments

       # def mark_as_complete(task)
       # Parameters: task
       # Side effects: changes incomplete status to complete
           
     