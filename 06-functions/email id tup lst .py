lst=[]
n=int(input("How many students? "))
for i in range(1,n+1):
    email=input("Enter email id of student"+str(i)+":")
    lst.append(email)
    etuple=tuple(lst)
lst1=[]
lst2=[]
for i in range(n):
    email=etuple[i].split('@')
    lst1.append(email[0])
    lst2.append(email[1])
unameTup=tuple(lst1)
dnameTup=tuple(lst2)
print("Student email ids :- ")
print(etuple)
print("User name tuple :- ")
print(unameTup)
print("Domain name tuple :- ")
print(dnameTup)
