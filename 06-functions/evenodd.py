a=input("Enter The Number ==> ")
even=[]
odd=[]
for i in a:
    i=int(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even ==> ",even)
print("Odd ==> ",odd)
