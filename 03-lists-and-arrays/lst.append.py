lst=[]
r=int(input("Enter the number of rows? "))
c=int(input("Enter the number of columns? "))
for i in range(r):
    row=[]
    for j in range(c):
        elem=int(input("Element"+str(i)+","+str(j)+":"))
        row.append(elem)
    lst.append(row)
print("List created is : ",lst)
