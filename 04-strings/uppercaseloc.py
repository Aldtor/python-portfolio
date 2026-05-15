a=input("Enter The Line ==> ")
x=y=d=0
for i in a:
    if i.isupper():
        x=x+1
    if i.islower():
        y=y+1
    if i.isdigit():
        d=d+1
print("Upper Case ==> ",x)
print("Lower Case ==> ",y)
print("No. of digits ==> ",d)
