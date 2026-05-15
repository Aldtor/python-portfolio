def bookad(x):
    a=["BOOK A","BOOK B","BOOK C","BOOK D"]
    if(len(a)>=4):
        print("** OVERFLOW **")
    else:
        a.append(x)
        print(" BOOK ** Successfully Added **")

def bookde():
    a=["BOOK A","BOOK B","BOOK C","BOOK D"]
    if(a==[]):
        print("** UNDERFLOW **")
    else:
        print("** Successfully Deleted **",a.pop())

print("1 :- push()")
print("2 :- pop()")
s=int(input("Enter Your Choice :- "))
if s==1:
    x=input("Enter The Book Name To Be Added ==> ")
    bookad(x)
if s==2:
    bookde()




