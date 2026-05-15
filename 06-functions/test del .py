z={2:"satyam", 244: 'somya',3:"ram"}
z2={}
rno=int(input("person ID ? "))
print('='*100)
print(z.keys())
if rno in z.keys():
    z.pop(rno,-1)
    z2=z
    print(z2)
    print(" ID :- ",rno,"Deleted from List.",z2)
else:
    print(" ID :- ",rno,"Does no exists in the List.")
    print('='*100)
    print("Final Person Detail List :- ")
    print(z)
    print('='*100)
    
