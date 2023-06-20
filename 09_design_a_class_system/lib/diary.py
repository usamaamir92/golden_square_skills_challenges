import re

class Diary():

    def __init__(self):
        self.diary_entries = []
        pass

    def add(self,diary_entry):
        self.diary_entries.append(diary_entry)

    def all(self):
        return self.diary_entries

    def get_readable_entry(self,wpm,minutes):
        words_able_to_read = wpm*minutes
        differences = {}
        readable_entries = []
        for entry in self.diary_entries:
            #differences[entry] = abs(len(entry.text.split())-words_able_to_read)
            differences[entry] = len(entry.text.split()) - words_able_to_read
        minimum_difference = min(differences.values())
        for key,value in differences.items():
            if value == minimum_difference and value <= 0:
                readable_entries.append(key)
        if readable_entries != []:
            return readable_entries
        else:
            return None

    
    def get_phone_numbers(self):
        phone_numbers = []
        for entry in self.diary_entries:
            phone_numbers += re.findall(r"0[0-9]{10}",entry.text)
        if phone_numbers != []:
            return phone_numbers
        else:
            return None
    
    def diary_entry_by_date(self,date):
        for entry in self.diary_entries:
            if date == entry.date:
                return entry

