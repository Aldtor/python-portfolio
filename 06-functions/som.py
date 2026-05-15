a=[]
fh=open("C:\\Users\\dell\\Desktop\\sam.txt","a")
n=int(input("enter the no. of details you want to add"))
for i in range(n):
    empid=int(input("enter the employee id"))
    nm=input("enter the employees name")
    post=input("enter the post")
    salary=float(input("enter the salary"))
    b=str(empid)+" "+ nm+" "+post+" "+ str(salary)
    a.append(b+"\n")
fh.writelines(a)
print("the details are successfully added")
fh.close()
    
    
