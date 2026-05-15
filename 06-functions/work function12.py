#1
'''def func(message,num=1):
    print(message*num)

func("Python")
func("Easy",3)'''

#2
'''def fun(s):
    k=len(s)
    m=" "
    for i in range(0,k):
        if(s[i].isupper()):
            m=m+s[i].lower()
        elif(s[i].isalpha()):
            m=m+s[i].upper()
        else:
            m=m+"bb"
    print(m)

fun('Schoo1234@com')'''

#3
'''def Change(P,Q=30):
    P=P+Q
    Q=P-Q
    print(P,"#",Q)
    return(P)

R=150
S=100
R=Change(R,S)
print(R,"#",S)
S=Change(S)'''

#4
'''def check(n1=1,n2=2):
    n1=n1+n2
    n2+=1
    print(n1,n2)

check()
check(2,1)
check(3)'''

#5
'''def Diff(N1,N2):
    if N1>N2:
        return N1-N2
    else:
        return N2-N1
NUM=[10,23,14,84,64]
for CNT in range(4,0,-1):
    A=NUM[CNT]
    B=NUM[CNT-1]
    print(Diff(A,B),"#",end=" ")'''

#6
'''def interest(prnc,time=2,rate=0.10):
    return (prnc*time*rate)
print(interest(6100,1))
print(interest(5000,rate=0.05))
print(interest(5000,3,0.12))
print(interest(time=4,prnc=5000))'''

#7
def getOnes(num):
    #return the ones digit of the integer num
    onesDigit = num%10
    return onesDigit

num=int(input("Enter The Number ==> "))
x=getOnes(num)
print(x)









