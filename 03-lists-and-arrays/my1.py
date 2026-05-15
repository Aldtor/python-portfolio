my1=[2,4,6]
print("Existing list is:- ",my1)
n=eval(input("Enter the number or list to be append: "))
if type(n)==type([]):#if a list is input
    my1.extend(n)
elif type(n)==type(1):#if a integer is input
    my1.append(n)
else:
    print("please enter either a integer or a list: ")
print("Append list is: ",my1)
