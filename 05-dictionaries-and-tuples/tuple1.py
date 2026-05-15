a=input("Enter mix of vowel and consonant")
print("Your input:- ",a)
b=('a','e','i','o','u')
for i in b:
    if i in a:
        print("vowel",i)
    else:
        print("Consonant \t",i)
