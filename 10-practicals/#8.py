#8. Write a program using python to get 10 players nameand their score.Write 
#the input in a csv file. Accept a player name using python.Read the csv file 
#to display the name and the score.If the player name is not found give an 
#appropriate message.

import csv
with open('C:\\Users\\dell\\Desktop\\player.csv','w') as f:
    w = csv.writer(f) 
    n=1
    while (n<=10):
        name = input("Player Name?:" )
        score = int(input("Score: "))
        w.writerow([name,score])
        n+=1
print("Player File created") 
f.close()
searchname=input("Enter the name to be searched ")
f=open('C:\\Users\\dell\\Desktop\\player.csv','r')
reader =csv.reader(f)
lst=[]
for row in reader:
    lst.append(row) 
q=0
for row in lst:
    if searchname in row:
        print(row)
        q+=1
    if(q==0):
        print("string not found")
f.close()
