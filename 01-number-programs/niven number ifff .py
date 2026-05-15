a=int(input("Enter the number :- "))
b=str(a)
d=0
for i in b:
    c=int(i)
    d=d+c
if(a%d==0):
    print("It is a niven number ")
else:
    print("It is not a Niven Number")
