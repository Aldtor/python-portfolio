a=input("ENter a line")
lc=uc=0
dc=ac=sc=0
for i in a:
     -if i.islower():
        lc+=1
    if i.isupper():
        uc+=1
    if i.isdigit():
        dc+=1
    if i.isalpha():
        ac+=1
    if i.isalnum()!=True and i !=' ':
        sc+=1
print("number of lower case letter..",lc)
print("number of upper case letter..",uc)
print("number of digit count letter..",dc)
print("number of alpha count letter..",ac)
print("number of symbol count count letter..",sc)
