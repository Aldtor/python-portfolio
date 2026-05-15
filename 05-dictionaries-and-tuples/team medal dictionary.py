team=[]
medal=[]
for a in range(5):
    tea,med=eval(input("Enter Students Name :- ,Enter Marks Scored :- "))
    team.append(tea)
    medal.append(med)
d={team[0]:medal[0],team[1]:medal[1],team[2]:medal[2],team[3]:medal[3],team[4]:medal[4]}
print("Created Dictionary")
print(d)
