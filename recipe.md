Excercise 1

1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2. Design the Function Signature

The function will be called estimate_reading_time.

The function will take one argument - a text string, and will return a float representing the number of minutes it will take to read the text.

3. Create Examples as Tests

Given a text of 200 words the function will return 1 minute.
estimate_reading_time("...(200 words)")
=> 1.0

Given a text of 300 words the function will return 1 minute.
estimate_reading_time("...(200 words)")
=> 1.5

Given a text of 400 words the function will return 1 minute.
estimate_reading_time("...(200 words)")
=> 2.0

Given a text of 0 words the function will return an error.
estimate_reading_time(")
=>error message ("Can't estimate time for empty text.")

4. Implement the Behaviour


Excercise 2

1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature

The function will be called verify_grammar. It will take one argument - a string of text, and will return True if the conditions are met, otherwise False.


3. Create Examples as Tests

Given the following text "Hello my name is Usama.":
The function will return True.

Given the following text "Hello my name is Usama!":
The function will return True.

Given the following text "Hello my name is Usama?":
The function will return True.

Given the following text "Hello my name is Usama":
The function will return False.

Given the following text "hello my name is Usama.":
The function will return False.

Given an empty string the function will return error message "No text entered.".


4. Implement the Behaviour




