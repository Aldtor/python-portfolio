ans="y"
while(ans=="y"):
    s=input("enter a string")
    if (s==s[::1]):
        print(s,"is a palendrome")
    else:
        print("not a palendroe")
    ans=input("Do you want to continue (y/n)")
