# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        for i in range (len(self.text)-1, -1, -1):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
        return self.text