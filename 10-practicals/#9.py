#9. Create a sql table using python and accept 10 names and age .sort in descending
#   order of age and display.

import sqlite3
connection = sqlite3.connect("info.db") 
cursor = connection.cursor()
#cursor.execute("DROP Table student")
cursor.execute("create table student3(name, age)")
print("Enter 10 students names and their ages respectively:")
for i in range(10):
    who =[input("Enter Name:")]
    age =[int(input("Enter Age:"))] 
    n =len(who) 
    for i in range(n):
        cursor.execute("insert into student3 values (?, ?)", (who[i],age[i])) 
cursor.execute("select * from student3 order by age desc") 
print("Displaying All the Records From student Table in Descending order of age")
print (*cursor.fetchall(),sep='\n' )
