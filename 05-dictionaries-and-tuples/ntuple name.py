lst=[]
n= int(input("How many students? "))
for i in range(1,n+1):
    name=input("Enter name of student"+str(i)+":-" )
    lst.append(name)
ntuple=tuple(lst)
nm=input("Enter name to be searched for :- ")
if nm in ntuple:
    print(nm,"exists in the tuple")
else:
    print(nm,"does not exists in the tuple")
