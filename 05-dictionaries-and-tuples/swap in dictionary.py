'''D={'a':2,'b':3,'c':1}
E={}
for c in D:
    E[D[c]]=c
print("Original Dictionary",D)
print(E)'''

s=0
d1={"cat":12,"dog":6,"elephant":23,\"bear":20}
for a in d1:
    if len(a)>3:
        s=s+d1[a]
print(s)
             
