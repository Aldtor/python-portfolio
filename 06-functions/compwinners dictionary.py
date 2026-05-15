n=int(input("Enter the number of students :- "))
compwinners={}
for a in range(n):
    key=int(input("Enter the students roll number :- "))
    value=int(input("Enter the score obtained :- "))
    print('='*100)
    compwinners[key]=value
print("The Dictionary formed is :- ")
print(compwinners)
print('='*100)
ans="y"
while(ans=='y'):
    rno=int(input("Roll No. to be deleted ? "))
    print('='*100)
    if rno in compwinners:
        del compwinners[rno]
        print("Roll NO. :- ",rno,"Deleted from dictionary.")
    else:
        print("Roll No. :- ",rno,"Does no exists in dictionary.")
    print('='*100)
    print("Final Dictionary :- ")
    print(compwinners)
    print('='*100)
    ans=input("do you want to delete more (y/n)")



    
