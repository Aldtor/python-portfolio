#a=[1,2,3,4,5,6,7,8,9,19]
#for i in a:
    #if(i%2==0):
        #print("Even",i)
    #else:
       # print("odd",i)
'''a=eval(input("input a list of numbers "))
for i in a:
    if(i%2==0):
        print("even",i)
        print("adding 5 ",i+5)
    else:
        print("odd",i)
        print("removing 3 ",i-3)'''
'''a=list(input("Enter a word:- "))
b=['a','e','i','o','u','A','E','I','O','U']
c=0
d=0
e=0
for i in a:
    if (i==' ' or i>='0' or i<='9'):
        e=e+1
    if i in b:
        d=d+1
        print("found vowel",i)
    else:
        c=c+1
        print("found consonat \t",i)
c=c-e
print("number of vowels - ",d)    
print("numbers of consonant found - ",c)'''

a=list(input("Enter a first list:- "))
b=list(input("Enter a second list:- "))       
c=(a+b)
print("The concatination of 2 list",c)
print("The replicate of 2 list",c*5)

       

