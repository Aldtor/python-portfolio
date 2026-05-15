val=eval(input("Enter a list:- "))
print("The original list:- ",val)
s=len(val)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    print(i,i+1)
    val[i],val[i+1]=val[i+1],val[i]
print("List after swapping:- ",val)
