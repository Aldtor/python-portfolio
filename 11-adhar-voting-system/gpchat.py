import webbrowser as wb
from datetime import date

today = date.today()
print("                                                   GOVERNMENT OF INDIA")
print("Date:- ", today, "                                                                                            SERVER-1")

name = input("Enter The Name ==> ")
aid = input("Enter The Aadhaar No ==> ")

# Simulating the adme function from adhar module
def adme(name, aid):
    print(f"Name: {name}, Aadhaar No: {aid}")

adme(name, aid)

file_path = "C:\\Users\\dell\\Desktop\\adhar\\aadhaar-card.html"

# Read the HTML file
with open(file_path, 'r', encoding='utf-8') as fh:
    content = fh.read()

# Replace the placeholders with the actual values
new_content = content.replace("Name: SATYAM KUMAR", f"Name: {name}")
new_content = new_content.replace("Aadhaar No: 1234 5678 9101", f"Aadhaar No: {aid}")

# Write the changes back to the file
with open(file_path, 'w', encoding='utf-8') as fh:
    fh.write(new_content)

print("Updated HTML content:")
print(new_content)

print("Do You Want To See Your Adhar Card ==> ")
print("[ y/n ]")
see = input("Enter Your Choice ==> ")
if see.lower() == 'y':
    w = "file:///C:/Users/dell/Desktop/adhar/aadhaar-card.html"
    wb.open(w)
