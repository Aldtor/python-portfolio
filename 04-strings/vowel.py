def checkvc():
    a=input("Enter the String (For Vowel and Consonant) :- ")
    b=['A','E','I','O','U']
    a.upper()
    for i in a:
        if i in b:
            print("It is a Vowel.")
        else:
            print("It is Consonant.")
checkvc()
