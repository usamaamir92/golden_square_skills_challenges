# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.list_todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.list_todos.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = []
        for todo in self.list_todos:
            if todo.complete == False:
                incomplete_todos.append(todo)
        return incomplete_todos

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = []
        for todo in self.list_todos:
            if todo.complete == True:
                complete_todos.append(todo)
        return complete_todos


