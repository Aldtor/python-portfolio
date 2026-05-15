#7. '''Write a program to accept a string and print the number of uppercase, lowercase, vowels, consonants and spaces in the given
# string using Class.

class String:
    def __init__(self):
        self.uppercase = 0
        self.lowercase = 0
        self.vowels = 0
        self.consonants = 0
        self.spaces = 0
        self.string = ""

    def getstr(self):
        self.string = input("Enter a String: ")

    def count_upper(self):
        for ch in self.string:
            if ch.isupper():
                self.uppercase += 1

    def count_lower(self):
        for ch in self.string:
            if ch.islower():
                self.lowercase += 1

    def count_vowels(self):
        for ch in self.string:
            if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
                self.vowels += 1

    def count_consonants(self):
        for ch in self.string:
            if ch.isalpha() and ch.lower() not in ('a', 'e', 'i', 'o', 'u'):
                self.consonants += 1

    def count_space(self):
        for ch in self.string:
            if ch == " ":
                self.spaces += 1

    def execute(self):
        self.count_upper()
        self.count_lower()
        self.count_vowels()
        self.count_consonants()
        self.count_space()

    def display(self):
        print("The given string contains...")
        print(f"{self.uppercase} Uppercase letters")
        print(f"{self.lowercase} Lowercase letters")
        print(f"{self.vowels} Vowels")
        print(f"{self.consonants} Consonants")
        print(f"{self.spaces} Spaces")


S = String()
S.getstr()
S.execute()
S.display()

