#4. Write a program to create a mirror of the given string. For example, "wel" = "lew".

def rev(str1):
    str2 = ""
    i = len(str1) - 1
    while i >= 0:
        str2 += str1[i] 
        i -= 1
    return str2

word = input("\nEnter a String ==> ")
print("\nThe Mirror image of the given string is:", rev(word))
