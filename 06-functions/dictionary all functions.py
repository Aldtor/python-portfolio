import json
n=int(input("Enter The Number Of People :- "))
coon=n
z1={"'ID':'rooln'":{'NAME':'a','GENDER':'b','Age':'c','QUALIFICATION':'d','WORKING EXPERIENCE':'f'}}
z={}
z2={}
print('='*100)
for i in range(n):
    rolln=int(input("Enter The ID Of The Person :- "))
    a=input("Enter Full Name Of The Person :- ")
    b=input("Enter The Gender Of The Person :- ")
    c=int(input("Enter The Age Of The Person :- "))
    d=input("Enter Your Qualifications :- ")
    print("Do You Have Any Past Experience :- ")
    print('='*100)
    e=input("Choose (y/n) :- ")
    choose="y"
    if (e=="y"):
        f=int(input("Enter How Many Years You Worked There ('ENTER THE NUMERIC VALUE') :- "))
    else:
        f=0
    print('='*100)
    coon=(coon-1)
    print(coon,"- More Input Needed")
    print('*'*100)
    z[rolln]=[a,b,c,d,f]
    print('='*100)
print("dictionary..",z)
verf="This is for Verification"   
print("This is for Verification")
ver=int(input("How many words :- "))
verfi=len(verf)
if (verfi==ver):
    print("Verified..")
print('='*100)
print("The Person Details Are..")
print(json.dumps(z,indent=5))
print('='*100)
print("Do You Want To Edit The List(yes/no)")
edit=input("Enter Your Choice :- " )
while(edit=='yes'):
    print("Choose Your Choice")
    print("min-(for the person details having lowest id)")
    print("max-(for the person details having highest id)")
    print("sort-(for arranging the list in ascending order)")
    print("sord-(for arranging the list in decending order)")
    print("del-(for deleting a person details)")
    print("upd-(for adding a person details in the list)")
    ch=input("Enter The Choice :- ")
    if (ch=='del'):
        rno=int(input("person ID ? "))
        print('='*100)
        if rno in z.keys():
            z.pop(rno)
            z2=z
            print(z2)
            print(" ID :- ",rno,"Deleted from List.",z2)
        else:
            print(" ID :- ",rno,"Does no exists in the List.")
            print('='*100)
            print("Final Person Detail List :- ")
            print(z)
            print('='*100)
    if (ch=='min'):
        mi=min(z)
        print(mi)
    if (ch=='max'):
        ma=max(z)
        print(ma)
    if (ch=='sort'):
        so=sorted(z)
        print(so)
    if (ch=='sord'):
        sod=sorted(z,reverse=True)
        print(sod)
    if (ch=='upd'):
        print("Enter The Details ex:-(id:'Name','Gender',Age,'Qualification',Working Experience(In Years)):- ")
        upd1={1:'rehan',"Gender":"Male","Age":45,"Qualification":"NA","Working Experience":4}
        up=z.update(upd1)
        print("The Details Are :- ",upd1)
        print('='*100)
        print("Final Person Detail List :- ")
        print(z)
    else:
        print("Your Final List Is :- ",z)
    edit=input("Do You Want To Edit More (yes/no) :- " )
else:
    print("Final Person Detail List :- ")
    print(z)












        
    



