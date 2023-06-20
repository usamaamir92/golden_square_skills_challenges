from lib.task_manager import *
import pytest

"""1. Describe the Problem
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
The interface of a class includes:

The name of the class.
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have
Steps 3 and 4 then operate as a cycle.

Name of the class will be TaskManager.
The __init__ method will need a variable for outstanding tasks in list format.
There will be an add method that takes a string and won't return anything.
There will be a list method that takes no arguments and returns the list of tasks outstanding.
There will be a remove method that takes a string and won't return anything.

3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

Test to check that the add method uses the given string and adds it to 
the task list variable (classname.task_list)."""

def test_task_manager_add():
    new_manager = TaskManager()
    new_manager.add("Vacuum")
    result = new_manager.task_list
    assert result == ["Vacuum"]


#Test to check that the list method returns the correct list of tasks 
#with single task.

def test_task_manager_single():
    new_manager = TaskManager()
    new_manager.add("Vacuum")
    result = new_manager.list()
    assert result == ["Vacuum"]

#Test to check that the list method returns the correct list of tasks 
#with multiple tasks (will need to call the add function multiple times).

def test_task_manager_multiple():
    new_manager = TaskManager()
    new_manager.add("Vacuum")
    new_manager.add("Washing up")
    result = new_manager.list()
    assert result == ["Vacuum","Washing up"]

#Test to check that the remove method removes the task from the task 
#list variable (classname.task_list).

def test_task_manager_remove():
    new_manager = TaskManager()
    new_manager.add("Vacuum")
    new_manager.add("Washing up")
    new_manager.remove("Vacuum")
    result = new_manager.task_list
    assert result == ["Washing up"]

#Test to raise exception for empty string on add method.

def test_task_manager_empty_string():
    new_manager = TaskManager()
    with pytest.raises(Exception) as e:
        new_manager.add("")
    error_message = str(e.value)
    assert error_message == "No task provided."


#Test to raise exception for non string data type on add method.

def test_task_manager_non_string():
    new_manager = TaskManager()
    with pytest.raises(Exception) as e:
        new_manager.add(12)
    error_message = str(e.value)
    assert error_message == "Not a string."

#Test to raise exception if given task doesnt exist in the list 
#variable on remove method.

def test_task_manager_no_such_task():
    new_manager = TaskManager()
    new_manager.add("Vacuum")
    with pytest.raises(Exception) as e:
        new_manager.remove("Mop")
    error_message = str(e.value)
    assert error_message == "No such task."

#4. Implement the Behaviour
#For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

#At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

#Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier."""

