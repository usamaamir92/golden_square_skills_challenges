class TaskManager():
    def __init__(self):
        self.task_list = []

    def add(self, string):
        if string == "":
            raise Exception("No task provided.")
        elif type(string) != str:
            raise Exception("Not a string.")
        self.task_list.append(string)

    def list(self):
        return self.task_list

    def remove(self, string):
        if string not in self.task_list:
            raise Exception("No such task.")
        self.task_list.remove(string)
    

