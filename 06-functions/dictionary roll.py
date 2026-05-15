M={}
n=int(input("How many students ?"))
for a in range(n):
    r,m=eval(input("Enter Roll No. , Marks :"))
    M[r]=m
print("Created dictionary")
print(M)
print("To Modify Marks")
r= int(input("Enter roll number :- "))
if r in M:
    M[r]=float(input("Enter new marks :- "))
else:
    print("No such roll no. found")
print("Modified dictionary is")
print(M)
