print("-"*130 )
print("                                       WELCOME TO LEARN ABOUT PYTHON                               ")
print("-"*130 )
name=input("enter your name")
while True:
    print("                                            choice 1=to use arithemetic operatios")
    print("                                            choice 2=to use relational operators")
    print("                                            choice 3=to use different types of numbers and programs")
    print("                                            choice 4=to use diffrent types of nested loops")
    ch=int(input("enter your choce with which you want to proceed"))
    if(ch==1):
        print("-"*130 )
        print("                                ENJOY ARITHEMETIC OPERATIONS")
        print("-"*130 )
        print("                                choice 1=to use '+' ")
        print("                                choice 2=to use '-' ")
        print("                                choice 3=to use '*' ")
        print("                                choice 4=to use '**' ")
        print("                                choice 5=to use '/' ")
        print("                                choice 6=to use '//' ")
        print("                                choice 7=to use '%' ")
        ch1=int(input("enter the choice with which arithemetic function you want to continue "))
        if(ch1==1):
            b=0
            n1=int(input("enter with how many numbers you want to perform arithemetic operations "))
            for c in range(n1):
                d=int(input("enter the number to perform arithemetic operations"))
                b=b+d
            print("sum is ",b)
        if(ch1==2):
             e=0
             n2=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for f in range(n2):
                 g=int(input("enter the number to perform arithemetic operations"))
                 e=e-g
             print("difference is ",e)
        if(ch1==3):
             h=0
             n3=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for i in range(n3):
                 j=int(input("enter the number to perform arithemetic operations"))
                 h=h*j
             print("product is ",h)
        if(ch1==4):
             k=0
             n4=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for l in range(n4):
                 m=int(input("enter the number to perform arithemetic operations"))
                 k=k**m
             print("exponentiation is ",k)
        if(ch1==5):
             n=0
             n5=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for o in range(n5):
                 p=int(input("enter the number to perform arithemetic operations"))
                 n=n/p
             print("division is ",)
        if(ch1==6):
             q=0
             n6=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for r in range(n6):
                 s=int(input("enter the number to perform arithemetic operations"))
                 q=q//s
             print("floor division is ",)
        if(ch1==7):
             t=0
             n7=int(input("enter with how many numbers you want to perform arithemetic operations "))
             for u in range(n7):
                 v=int(input("enter the number to perform arithemetic operations"))
                 t=t%v
             print("remainder is ",)
    if(ch==2):
        print("-"*130 )
        print("                                ENJOY RELATIONAL OPERATIONS")
        print("-"*130 )
        print("                                choice 1=to use '>' ")
        print("                                choice 2=to use '<' ")
        print("                                choice 3=to use '==' ")
        print("                                choice 4=to use '>=' ")
        print("                                choice 5=to use '<=' ")
        print("                                choice 6=to use '!=' ")
        print("                                choice 7=to know about 'and' ")
        print("                                choice 8=to know about 'or' ")
        print("                                choice 9=to know about 'not' ")
        ch2=int(input("enter the choice with which relational function you want to continue "))
        if(ch2==1):
            a=int(input("enter a number"))
            b=int(input("enter the second number"))
            print("a>b=",a>b)
        if(ch2==2):
            c=int(input("enter a number"))
            d=int(input("enter the second number"))
            print("c<d=",c<d)
        if(ch2==3):
            e=int(input("enter a number"))
            f=int(input("enter the second number"))
            print("e==f=",e==f)
        if(ch2==4):
            g=int(input("enter a number"))
            h=int(input("enter the second number"))
            print("g>=h=",g>=h)
        if(ch2==5):
            i=int(input("enter a number"))
            j=int(input("enter the second number"))
            print("i<=j=",i<=j)
        if(ch2==6):
            k=int(input("enter a number"))
            l=int(input("enter the second number"))
            print("k!=l=",k!=l)
        if(ch2==7):
            print("A      | B       | A AND B")
            print("-------|---------|---------")
            for a in [True, False]:
                for b in [True, False]:
                    c=(a and b)
                    print(f"{a}   | {b}     | {c}")
        if(ch2==8):
            print("A      | B       | A OR B")
            print("-------|---------|---------")
            for a in [True, False]:
                for b in [True, False]:
                    c=(a or b)
                    print(f"{a}   | {b}     | {c}")

        if(ch2==9):
            print("A      | NOT A")
            print("-------|---------")
            for a in [True, False]:
                c=(not a)
                print(f"{a}   |{c}")
    if(ch==3):
        print("-"*130 )
        print("                                ENJOY DIFFERENT TYPES OF NUMBERS")
        print("-"*130 )
        print("                                choice 1= ARMSTRONG NUMBER","\n( Armstrong number is a number that is equal to the sum of cubes of its digits)")
        print("                                choice 2= NIVEN NUMBER","\n( Niven number is a number that is evenly divisible by the sum of its digits.)")
        print("                                choice 3= PALINDROME NUMBER","\n( Palindrome number is the number or string must be the same when inverted.)")
        print("                                choice 4= BUZZ NUMBER","\n(Buzz number is the number if it ends with 7 OR is divisible by 7.)")
        print("                                choice 5= SPY NUMBER","\n(Spy number is the number if the sum of its digits is exactly equal to the product of its digits.)")
        print("                                choice 6= PRIME NUMBER","\n(Prime number is the number which has no other  factor than 1 and the number itself.)")
        print("                                choice 7= PERFECT NUMBER","\nPerfect number is the sum of its positive divisors")
        print("                                choice 8= TECH NUMBER ","\n(Tech number is a number that has an even number of digits.)")
        print("                                choice 9= LEAD NUMBER ","\nLead number is the number if the sum of even digit is equal to the sum of odd digits")
        print("                                choice 10= MAGIC NUMBER ","\nMagic number is a numeric value that appears directly in the code without any explanation")
        print("                                choice 11= ODD EVEN NUMBER ","\n(Odd number is a number which is not divisible by 2.)","\n(Even number is a number which is divisible by 2.)")
        print("                                choice 12= FIBONACCI SERIES ","\n(Fibonacci series is a mathematical sequence that starts with 0 and 1, with each subsequent number being the sum of the two preceding ones.)") 
        ch3=int(input("enter the choice with which type of number you want to continue "))
        if(ch3==1):
            a=int(input("enter a number :- "))
            b=a
            c=d=e=0
            while(a>0):
                d=a%10
                c=d*d*d
                e=e+c
                a=a//10
            if(b==e):
                print("it's an armstrong number")
            else:
                print("it's NOT an armstrong number ")
        if(ch3==2):
            a1=int(input("enter the number :- "))
            b1=a1
            c1=0
            while(a1>0):
                d1=a1%10
                c1=c1+d1
                a1=a1//10
            if(b1%c1==0):
                print("it's a niven number")
            else:
                print("it's NOT a niven number")
        if(ch3==3):
            a2=int(input("enter the number :- "))
            b2=a2
            c2=0
            while(a2>0):
                d2=a2%10
                c2=c2*10+d2
                a2=a2//10
            if(b2==c2):
                print("it's a palindrome number")
            else:
                print("it's NOT a palindrome number")
        if(ch3==4):
            a3=int(input("enter the number :- "))
            if(a3%10==7 or a3%7==0):
                print("it's a buzz number")
            else:
                print("it's NOT a buzz number")
        if(ch3==5):
            a4=int(input("enter the number :- "))
            s=0
            p=1
            while(a4>0):
                x=a4%10
                s=s+x
                p=p*x
                a4==a4//10
            if(s==p):
                print("it's a spy number")
            else:
                print("it's NOT a spy number")
        if(ch3==6):
            a5=int(input("enter the number :- "))
            c5=0
            for i in range(1,a5+1):
                if(a5%i==0):
                    c5=c5+1
            if(c5==2):
                print("prime number")
            else:
                print("NOT a prime number")
        if(ch3==7):
            a6=int(input("enter the number :- "))
            b6=0
            s6=1
            for i in range(1,a6):
                if(a6%i==0):
                    b6=b6+i
                    s6=s6*i
                if(b6==a6 and s6==a6):
                    print("it's a perfect number")
                else:
                    print("it's NOT a perfect number")
        if(ch3==8):
            a7=int(input("enter the number :- "))
            b7=a7
            c7=0
            fh=0
            sh=0
            sq=0
            while(a7>0):
                c7=c7+1
                a7=a7//10
            if(c7%2==0):
                fh=b7%pow(10,c7//2)
                sh=b7//pow(10,c7//2)
                sq=(fh+sh)*(fh+sh)
            if(b7==sq):
                print("it's a tech number")
            else:
                print("it's NOT a tech number")
        if(ch3==9):
            a8=int(input("Enter the number :- "))
            ev=0
            od=0
            b8=0
            while(a8>0):
                b8=a8%10
                if(b8%2==0):
                    ev=ev+b8
                else:
                    od=od+b8
                a8=a8//10
            if(od==ev):
                print("Yes Lead Number")
            else:
                print("Not A Lead Number")
        if(ch3==10):
            b9=d9=0
            a9=int(input("Enter a number :- "))
            c9=a9
            v9=1
            h9=0
            while(c9>0):
                v9=1
                d9=c9%10
                for i in range(1,d9+1):
                    v9=v9*i
                h9=h9+v9
                c9=c9//10
            if(h9==a9):
                print("The number is a magic number")
            else:
                print("The number is NOT a magic number")
        if(ch3==11):
            a10=[]
            a10=eval(input("Enter the list"))
            ev=[]
            od=[]
            for i in a10:
                if(i%2==0):
                    ev.append(i)
                else:
                    od.append(i)
            print("even numbers are :- ",ev)
            print("odd numbers are :- ",od)
        if(ch3==12):
            n=int(input("Enter the number ==> "))
            a11=0
            b11=1
            print(a11,b11,end=' ')
            c11=1
            for i in range(n+1):
                if(c11<=n):
                    print(c,end=' ')
                    a11=b11
                    b11=c11
                    c11=a11+b11
    if(ch==4):
        print("-"*130 )
        print("                                ENJOY DIFFERENT TYPES OF NESTED LOOPS")
        print("-"*130 )
        print("                                choice 1=\n1","\n1 2","\n1 2 3")
        print("                                choice 2=\n1","\n2 2","\n3 3 3 ")
        print("                                choice 3= \n*","\n* *","\n* * *")
        print("                                choice 4= \n* #","\n* # * #","\n* # * # * #")
        print("                                choice 5= \n* ","\n* # ","\n* # * ")
        print("                                choice 6=\n1","\n2 3","\n4 5 6 ")
        print("                                choice 7=\nA","\nA B","\nA B C ")
        print("                                choice 8=\nA","\nB C","\nD E F  ")
        print("                                choice 9=\nA","\nB B","\nC C C  ")
        ch4=int(input("enter the choice with which type of nested loop you want to continue "))
        if(ch4==1):
            n=int(input("enter the number of times you want"))
            for i in range (1,n):
                for j in range(1,i+1):
                    print(j,end=" ")
                print("\n")
        if(ch4==2):
            n1=int(input("enter the number of times you want"))
            for i in range (1,n1):
                for j in range(1,i+1):
                    print(i,end=" ")
                print("\n")
        if(ch4==3):
            n2=int(input("enter the number of times you want"))
            for i in range (1,n2):
                for j in range(1,i+1):
                    print("*",end=" ")
                print("\n")
        if(ch4==4):
            n3=int(input("enter the number of times you want"))
            for i in range (1,n3):
                for j in range(1,i+1):
                    print("*",end=" #")
                print("\n")
        if(ch4==5):
            n4=int(input("enter the number of times you want"))
            for i in range (1,n4):
                for j in range(1,i+1):
                    if(j%2!=0):
                        print("*",end=" ")
                    else:
                        print("#",end=" ")
                print("\n")
        if(ch4==6):
            n5=int(input("enter the number of times you want"))
            k=1;
            for i in range (1,6):
                for j in range(1,i+1):
                    print(k,end=" ")
                    k=k+1
                print("\n")
        if(ch4==9):
            n8=int(input("enter the number of times you want"))
            n9=65
            for i in range(0,n8):
                for j in range(0,i+1):
                    j=chr(n9)
                    print(j,end=" ")
                n9=n9+1
                print("\n")
        if(ch4==8):
            n6=int(input("enter the number of times you want"))
            n7=65
            for i in range(0,n6):
                for j in range(0,i+1):
                    ch=chr(n7)
                    print(ch,end=" ")
                    n7=n7+1
                print("\n")
        if(ch4==7):
            n10=int(input("enter the number of times you want"))
            for i in range (65,n10+65):
                for j in range(65,i+1):
                    print(chr(j),end=" ")
                print()
                print("\n")
    dy=input("\ndo you want to continue ? [y/n]: ")
    if dy=="n":
         break
    else:
        pass
print("-"*130 )
print("\n THANK YOU",name,"\npowered by SOMYA KUMARI ", "\nunder the guidance of MR.RAVI KUMAR SINGH")
print("-"*130 )





















        
