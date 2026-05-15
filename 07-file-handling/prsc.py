import pickle
fh=open("C:\\Users\\dell\\Desktop\\emp.dat","wb")
x={}
for i in range(5):
    a=input("Enter The Name ==> ")
    b=int(input("Enter The Age ==> "))
    c=input("Enter The Designation ==> ")
    d=input("Enter The Salary ==> ")
    e=input("Enter The Work Experiece ==> ")
    x['name']=a
    x['age']=b
    x['Designation']=c
    x['Work Experience']=e
    x['Salary']=d
    pickle.dump(x,fh)
fh.close()
