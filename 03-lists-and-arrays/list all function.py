import json
print('='*114)
print("                                                 Appointement Form")
print('='*114)
n=int(input("Enter The Number Of People :- "))
j=n
l=[]
print('='*100)
for i in range(n):
    a=input("Enter Full Name Of The Patient :- ")
    e=input("Enter Your Email Id :- ")
    f=input("Enter Your Phone Number :- ")
    b=input("Enter The Gender Of The Patient :- ")
    c=int(input("Enter The Age Of The Patient :- "))
    d=input("Enter The Appointment Time **(Between 4pm to 10pm **):- ")
    h=input("Health Insurance (Yes/No) :- ")
    print("Which procedure do you want to make an appointment for ? ")
    print('='*100)
    print("Input - mx(Medical Examination),dc(Doctor Check),ra(Result Analysis),cu(Check-up)")
    g=input("Input From Above :- ")
    if (g=="mx"):
        g="Medical Examination"
    if (g=="dc"):
        g="Doctor Check"
    if (g=="ra"):
        g="Result Analysis"
    if (g=="cu"):
        g="Check-up"
    else:
        print("Wrong Input!!...............")
    print('*'*100)
    x="Name :- "+a+" "+"Email-Id:- "+e+" "+"Phone Number:- "+f+" "+"Gender:- "+b+" "+"Age:- "+str(c)+" "+"Appointement Time:- "+d+" "+h+" "+"appointment for:- "+g
    l.append(x)
print(json.dumps(l,indent=5))
eawwaewak=list(x)
i=input("How did you hear of us ? ")
j=(j-1)
print(j,"more input required")
print("to feed more appointment (ap)")
print("to see all appointments feeded(ds)")
ch=input("enter your choice")
if (ch=="ap"):
    ans='y'
    n1=int(input("Enter The Number Of People :- "))
    while(ans=='y'):
        for i in range(n1):
            a=input("Enter Full Name Of The Patient :- ")
            e=input("Enter Your Email Id :- ")
            f=input("Enter Your Phone Number :- ")
            b=input("Enter The Gender Of The Patient :- ")
            c=int(input("Enter The Age Of The Patient :- "))
            d=input("Enter The Appointment Time **(Between 4pm to 10pm **):- ")
            h=input("Health Insurance (Yes/No) :- ")
            print("Which procedure do you want to make an appointment for ? ")
            print('='*100)
            print("Input - mx(Medical Examination),dc(Doctor Check),ra(Result Analysis),cu(Check-up)")
            g=input("Input From Above :- ")
            if (g=="mx"):
                g="Medical Examination"
            if (g=="dc"):
                g="Doctor Check"
            if (g=="ra"):
                g="Result Analysis"
            if (g=="cu"):
                g="Check-up"
            else:
                print("Wrong Input!!...............")
            j=(j-1)
            print(j,"more input required")
        print('*'*100)
        x="Name :- "+a+" "+"Email-Id:- "+e+" "+"Phone Number:- "+f+" "+"Gender:- "+b+" "+"Age:- "+str(c)+" "+"Appointement Time:- "+d+" "+h+" "+"appointment for:- "+g
        l.append(x)
        print(json.dumps(l,indent=5))
        i=input("How did you hear of us ? ")
        ans=input("do you want to feed more appointments? [y/n]:   ")
if (ch=="ds"):
    print(x)
print("                              choice 1=pop()")
print("                              choice 2=clear()")
print("                              choice 3=count()")
print("                              choice 4=reverse()")
print("                              choice 5=sort()")
print("                              choice 6=sorted()")
print("                              choice 7=min()")
print("                              choice 8=max()")
print("                              choice 9=sum()")
print("                              choice 10=remove()")
ch=int(input("enter your CHOICE with which you want to continue"))
if(ch==1):

    
    
    
        












