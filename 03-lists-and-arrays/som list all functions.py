name=input("enter your name")
a=input("enter the string")
print("                              choice 1=len()")
print("                              choice 2=capitalize()")
print("                              choice 3=count()")
print("                              choice 4=find()")
print("                              choice 5=index()")
print("                              choice 6=isalnum()")
print("                              choice 7=isalpha()")
print("                              choice 8=isdigit()")
print("                              choice 9=islower()")
print("                              choice 10=isupper()")
print("                              choice 11=isspace()")
print("                              choice 12=upper()")
print("                              choice 13=lower()")
print("                              choice 14=lstrip()")
print("                              choice 15=rstrip()")
print("                              choice 16=strip()")
print("                              choice 17=startswith()")
print("                              choice 18=endswith()")
print("                              choice 19=istitle()")
print("                              choice 20=title()")
print("                              choice 21=replace()")
print("                              choice 22=join()")
print("                              choice 23=split()")
print("                              choice 24=partition()")
print("                              choice 25=swapcase()")
while True:
    ch=int(input("enter the choice you want to continue"))
    if (ch==1):
        print(len(a))
    if (ch==2):
        print(a.capitalize())
    if (ch==3):
        b=input("enter the sub-string you want to count the occurance")
        print(a.count(b))
    if (ch==4):
        c=input("enter the sub-string you want to find")
        print(a.find(c))
    if (ch==5):
        d=input("enter the string you want to find the index of")
        print(a.index(d))
    if (ch==6):
        print(a.isalnum())
    if (ch==7):
        print(a.isalpha())
    if (ch==8):
        print(a.isdigit())
    if (ch==9):
        print(a.islower())
    if (ch==10):
        print(a.isupper())
    if (ch==11):
        print(a.isspace())
    if (ch==12):
       print(a.upper())
    if (ch==13):
       print(a.lower())
    if (ch==14):
       print(a.lstrip())
    if (ch==15):
       print(a.rstrip())
    if (ch==16):
       print(a.strip())
    if (ch==17):
       e=input("enter the string you want to check the string starts with")
       print(a.startswith(e))
    if (ch==18):
       f=input("enter the string you want to check the string ends with")
       print(a.endswith(f))
    if (ch==19):
       print(a.istitle())
    if (ch==20):
       print(a.title())
    if (ch==21):
       g=input("enter the string with which you want to replace the old string")
       print(a.replace(a,g))
    if (ch==22):
       h=input("enter the symbol with which you want to join with the string")
       i=int(input("enter the number of terms of symbol you want to join with the string"))
       j=h*i
       print(j.join(a))
    if (ch==23):
       k=input("enter the string with which you want to split the old string")
       print(a.split(k))
    if (ch==24):
       l=input("enter the string with which you want to separate from the old string")
       print(a.partition(l))
    if (ch==25):
       print(a.swapcase())
    dy=input("\ndo you want to continue ? [yes/no]: ")
    if dy=="no":
        break
    else:
        pass
print("\n THANK YOU",name,"powered by SOMYA")














    
