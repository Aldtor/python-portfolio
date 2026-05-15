x=eval(input("Enter The Numbers ==> "))
print("Your List ==> ",x)
print("For Input 1 Item ( 1 )")
print("For Input more Item ( 2 )")
print("For Inserting At A Specific Position ( 3 )")
a=int(input("Enter Your Choice ==> "))
if(a==1):
    a1=input("Enter The Value To Be Added ==> ")
    x.append(a1)
    print("Updated List ==> ",x)
if(a==2):
    n=int(input("Enter The Number Of Value To Be Added ==> "))
    a1=input("Enter The Number Of Value To Be Added ==> ")
    a4=input("Enter The Number Of Value To Be Added ==> ")
    x.extend([a1,a4])
    print("Updated List ==> ",x)
if(a==3):
    a1=int(input("Enter The Position TO Specific Position ==> "))
    a2=int(input("Enter The Value"))
    x.insert(a1,a2)
    print("Updated List ==> ",x)

    
    
    
