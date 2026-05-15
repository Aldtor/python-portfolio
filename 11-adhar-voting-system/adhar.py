def adme(name ,aid):
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

#main



             
