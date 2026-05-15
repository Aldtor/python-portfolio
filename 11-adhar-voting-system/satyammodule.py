print(" 1 For Checking Prime Number")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


def prime(): #1
    c=0
    a=int(input("Enter The Number (for Prime) :- "))
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print("It is a Prime Number.")
    else:
        print("It is not a Prime Number.")
        
def armstrong(): #2
    s=0
    e=0
    a=int(input("Enter the Number (For Armstrong) :- "))
    x=a
    while(x>0):
        t=x%10
        e=t*t*t
        s=s+e
        x=x//10
    if(s==a):
        print("It is a Armstrong Number.")
    else:
        print("It is not a Armstrong Number.")

def sum(): #3
    a=int(input("Enter First Number (For Sum) :- "))
    b=int(input("Enter Second Number (For Sum) :- "))
    c=(a+b)
    print("The Sum Of Two Number is :- ",c)

def palendrome(): #4
    a=input("Enter The String (for Palendrome) :- ") 
    if (a==a[: : -1]):
        print(a," It is a Palendrome.")
    else:
        print("It is not a Palendroe")

def niven(): #5
    a=int(input("Enter the Number (For Niven) :- "))
    b=str(a)
    d=0
    for i in b:
        c=int(i)
        d=d+c
    if(a%d==0):
        print("It is a niven number. ")
    else:
        print("It is not a Niven Number.")

def checkvc(): #6
    a=input("Enter the String (For Vowel and Consonant) :- ")
    b=['A','E','I','O','U']
    a.upper()
    for i in a:
        if i in b:
            print("It is a Vowel.")
        else:
            print("It is Consonant.")

def duck(): #7
    a=input("Enter the Number (For Checking Duck Number) ==> ")
    l=len(a)
    c=0
    x=a[0:1]
    x=int(x)
    b=int(a)
    while(b>0):
        if(b%10==0):
            c=c+1
        b=b//10
    if(c>0 and x!=0):
        print("It is a Duck NUmber.")
    else:
        print("It is not a Duck Number.")

def fibonacciseries(): #8
    n=int(input("Enter the number (For No. Of Series) ==> "))
    a=0
    b=1
    print(a,b,end=' ')
    c=1
    print('='*100)
    while(c<=n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b

def adnme(name ,aid): #9 Adhar Card
    print("Do you have any correction")
    print("To Change Name[1] , To Change Id[2] ")
    ch=int(input("Enter The Choice ==> "))
    if (ch==1):
        verf=int(input("Enter Your Id For Verification => "))
        if(aid==verf):
            nm=input("Enter The New Name ==> ")
            name=nm
            print("New Name",name)
    if (ch==2):
        verf=int(input("Enter Your Id For Verification => "))
        if(aid==verf):
            aisd=int(input("Enter The New Name ==> "))
            aid=aisd
            print("New Id ",aisd)

def idpass(): #10 ID PASS
    import random
    import sys
    from colorama import Fore, Back, Style
    code=0
    ans="y"
    while(ans=="y"):
        usname=input("Choose the User Name :- ")
        print('='*50)
        sa=input(Fore.GREEN + ("Choose Passcode :- type / for random pass type:- random :- "))
        print('='*50)
        if(sa=="type"):
            code=int(input("Choose your Passcode :- "))
        elif(sa=="random"):
            code=(random.randrange(0,1000000))
            print("Your random password:- ",code)
        print('='*50)    
        print("Your date of birth in case of 'Password Recovery' ")
        print('='*50)
        date=(input("Enter the Date :- "))
        month=(input("Enter the Month :- "))
        year=(input("Enter the Year :- "))
        print('='*50)    
        fg=(date+month+year)
        print("Your Date Of Birth :- ",fg)
        print('='*50)    
        print("Verify you are not a Robot")
        print('='*50)    
        ys=int(input(" 2 + 3 :- "))    
        if(ys==5):
            print("Verified you are not a Robot")
        #else:
            #print("wrong answer verify again")
            ysg=chr(code)
    #if usname in code:
        #print("Your code should not\contain your u
            print("Thankyou")
            print('='*50)    
            print("Your user name :- ",usname)
            print('='*50)    
            print("Your encrypted password :- ॖॡॢॣ।॥०१-....",ysg)
            print('='*50)
            a=input("Enter your User Name :- ")
            print('='*50)    
            print("Enter Your Pass(input(inp))or Enter Your Date Of Birth(input(dob))")
            print('='*50)    
            ch=input("Enter Your Choice :- ")
            b=0
            bar=0
            if(ch=="inp"):
                b=int(input("Enter your Passcode :- "))        
            elif(ch=="dob"):
                bar=input("Enter Your Date Of Birth :- ")
            print('='*50)
            if usname==a and code==b or fg==bar:
                print("Thank You,You have entered the correct User Name and Passcode")
            else:
                print("Wrong Passcode or User Name")
            print('='*50)
            print('^'*50)
            if usname==a and code==b or fg==bar:
                print("Confidential Information:- 90+90=180")
                print('='*50)
            else:
                print('error^!'*1000)
            print('='*50)        
        ans=input("Do you want to continue (y/n)")




