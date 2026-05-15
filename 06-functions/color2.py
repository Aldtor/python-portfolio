import sys
from termcolor import colored,cprint
print(Fore.RED +'i am red' )
text=colored("hello","red",attrs=["reverse","blink"])
print(text)
