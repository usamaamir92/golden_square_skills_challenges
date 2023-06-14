class GrammarStats:
    def __init__(self):
        self.total_tests = 0
        self.tests_passed = 0
        self.tests_failed = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == "":
            raise Exception("No text provided.")
        elif type(text) != str:
            raise Exception("Not a string.")
        if text[0].isupper() and text[-1] in [".","!","?"]:
            self.total_tests += 1
            self.tests_passed += 1
            return True
        else:
            self.total_tests += 1
            self.tests_failed += 1
            return False
        
  
    def percentage_good(self):
        percentage_passed = round((self.tests_passed/self.total_tests)*100,2)
        return percentage_passed
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        