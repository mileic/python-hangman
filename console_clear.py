#Imports
from os import system, name
import time

def clear():

# for windows
if name == 'nt':
_ = system('cls')

# for mac and linux
else:
_ = system('clear')
 
time.sleep(3)
clear()
