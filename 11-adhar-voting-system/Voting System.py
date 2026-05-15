import adhar
from adhar import adme
import webbrowser as wb
import datetime
from datetime import date
today=date.today()
print("                                                   GOVERNMENT OF INDIA")
print("Date:- ",today,"                                                                                            SERVER-1")
name=input("Enter The Name ==> ")
aid=int(input("Enter The Id ==> "))
adme(name,aid)
fh=open("C:\\Users\\dell\\Desktop\\adhar\\aadhaar-card.html",'r+')
x=fh.readline()
print(fh.seek(1600))
print(fh.read(1600))
fh.write(satya)
'''for i in x:
    if(i=="<p><strong>Name:</strong> SATYAM KUMAR</p>"):
        fh.write("<p><strong>Name:</strong>" ,name,"</p>")'''
print(x)
print(x)
print("Do You Want To See Your Adhar Card ==> ")
print("[ y/n ]")
see=input("Enter Your Choice ==> ")
if (see=='y'):
    w= "file:///C:/Users/dell/Desktop/adhar/aadhaar-card.html"
    wb.open(w)




        
