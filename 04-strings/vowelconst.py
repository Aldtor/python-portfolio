x=input("Enter the String {Vowel and Consonant} ==> ")
a=['A','E','I','O','U']
c=0
b=0
x.upper()
for i in x:
    if(i==' '):
        continue
    if i in a:
        b=b+1
    else:
        c=c+1
print("Vowels ==> ",b)
print("Consonant ==> ",c)
x=input("Enter a String")
a=['a','e','i','o','u']
x=x.lower()
c=v=0
for i in x:
    if(i==' '):
        continue
    if(i in a):
        v=v+1
    else:
        c=c+1
print("vowels..",v)
print("consonant..",c)'''
s="computer application"
c=s.split()
print(c)
    
