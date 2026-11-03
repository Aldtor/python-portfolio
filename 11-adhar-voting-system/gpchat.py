import html
import webbrowser as wb
from datetime import date

today = date.today()
print("DEMO ONLY — not affiliated with UIDAI or the Government of India.")
print("Use fictional values only. This script writes the name and ID into a local HTML file.")
print("Aadhaar-style demo card")
print("Date:- ", today)

name = input("Enter a fictional demo name (do not use real personal information) ==> ")
aid = input("Enter a fictional demo ID (do not use a real Aadhaar number) ==> ")

# Simulating the adme function from adhar module
def adme(name, aid):
    print(f"Demo name: {name}, Demo ID: {aid}")

adme(name, aid)

file_path = "C:\\Users\\dell\\Desktop\\adhar\\aadhaar-card.html"

# Read the local demo HTML file
with open(file_path, 'r', encoding='utf-8') as fh:
    content = fh.read()

# HTML-escape the fictional values before inserting them into the local page.
new_content = content.replace("Name: SATYAM KUMAR", f"Name: {html.escape(name)}")
new_content = new_content.replace("Aadhaar No: 1234 5678 9101", f"Aadhaar No: {html.escape(aid)}")

# Write the changes back to the local demo HTML file
with open(file_path, 'w', encoding='utf-8') as fh:
    fh.write(new_content)

print("Updated demo HTML content:")
print(new_content)

print("Do You Want To See Your Demo Card ==> ")
print("[ y/n ]")
see = input("Enter Your Choice ==> ")
if see.lower() == 'y':
    w = "file:///C:/Users/dell/Desktop/adhar/aadhaar-card.html"
    wb.open(w)
