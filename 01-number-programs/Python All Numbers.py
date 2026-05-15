print('='*131)
print('='*131)
print("                                                 PYTHON ALL KIND OF NUMBERS")
print('='*131)
print('='*131)
print("              CHOOSE                       ")

print("           BUZZ NUMBER :- 1 ")
print("           PALINDROME :- 2 ")
print("           ARMSTRONG Number :- 3 ")
print("           Spy Number :- 4 ")
print("           Lead Number :- 5 ")
print("           Tech Number :- 6 ")
print("           Special Number :- 7 ")
print('='*131)
res="y"
while(res=="y"):
    ch=input("Enter Your Choice :- ")
    if(ch=="1"):
        print('='*131)
        print(">> A number is said to be Buzz Number if it ends with 7 OR is divisible by 7.")
        print('='*131)
        print("Now lets Start :- ")
        ans="y"
        while(ans=="y"):
            a=int(input("Enter the number of your choice :- "))
            if(a%7==0 or a%10==7):
                print("It is a Buzz Number.")
            else:
                print("It is not a Buzz Number.")
            print('='*131)
            ans=input("Do you want to check Buzz Number again (y/n)")
            print('='*131)
    if(ch=="2"):
        print('='*131)
        print(">> A number is said to be Palindrome if the number or string must be the same when inverted.")
        print('='*131)
        print("Now lets Start :- ")
        par="y"
        while(par=="y"):
            b=int(input("Enter the number of your choice :- "))
            c=b
            e=0
            l=len(str(b))
            for i in range(0,l):
                d=b%10
                e=e*10+d
                b=b//10
            if(c==e):
                print("It is a Palindrome.")
            else:
                print("It is not Palindrome.")
            print('='*131)
            par=input("Do you want to check Palindrome again (y/n)")
            print('='*131)
    if(ch=="3"):
        print('='*131)
        print(">> Armstrong number refers to those whose value is equal to the cube of each digits and overall its sum.")
        print('='*131)
        print("Now lets Start :- ")
        arm="y"
        while(arm=="y"):
            f=int(input("Enter the number of your choice :- "))
            g=f
            h=0
            while(f>0):
                t=f%10
                e=t*t*t
                h=h+e
                f=f//10
            if(h==g):
                print("It is a Armstrong Number.")
            else:
                print("It is not a Armstrong Number.")
            print('='*131)
            arm=input("Do you want to check Armstrong Number again (y/n)")
            print('='*131)
    if(ch=="4"):
        print('='*131)
        print(">> A number is said to be a Spy Number if the sum of all the digits is equal to the product of all digits. ")
        print('='*131)
        print("Now lets Start :- ")
        spy="y"
        while(spy=="y"):
            i=int(input("Enter the number of your choice :- "))
            j=0
            k=1
            while (i>0):
                m=i%10
                j=j+m
                k=k*m
                i=i//10
            if(j==k):
                print("It is a Spy Number.")
            else:
                print("It is not a Spy Number.")
            print('='*131)
            spy=input("Do you want to check Armstrong Number again (y/n)")
            print('='*131)
    if(ch=="5"):
        print('='*131)
        print(">> Lead Number is a number in which the sum of the even digits is equal to the sum of the odd digits. ")
        print('='*131)
        print("Now lets Start :- ")
        lea="y"
        while(lea=="y"):
            n=int(input("Enter the number of your choice :- "))
            x=0
            y=0
            o=0
            while(n>0):
                o=n%10
                if(o%2==0):
                    x=x+o
                else:
                    y=y+o
                    n=n//10
            if(y==x):
                print("It is a Lead Number.")
            else:
                print("It is not a Lead Number.")
            print('='*131)
            lea=input("Do you want to check Lead Number again (y/n)")
            print('='*131)
    if(ch=="6"):
        print('='*131)
        print(">> A Tech number is a number that has an even number of digits and if the number is split into two equal halves(From the middle), then the square of the sum of these halves is equal to the number itself.")
        print('='*131)
        print("Now lets Start :- ")
        tec="y"
        while(tec=="y"):
            print('='*131)
            tec=input("Do you want to check Lead Number again (y/n)")
            print('='*131)
            
     if(ch=="7"):
         print(">> .")
         print('='*131
         print("Now lets Start :- ")
         spe="y"
         while(spe=="y"):
             b=d=0
             a=int(input("Enter a number :- "))
             c=a
             v=1
             h=0
             while(c>0):
                 v=1
                 d=c%10
                 for i in range(1,d+1):
                     v=v*i
                 h=h+v
                 c=c//10
             if(h==a):
                 print("The number is a special number")
             else:
                 print("The number is not a special number")
             print('='*131)
             spe=input("Do you want to check Lead Number again (y/n)")
             print('='*131)
    res=input("Do you want to choose another choice (y/n)")
