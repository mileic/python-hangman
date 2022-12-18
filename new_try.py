#Imports
import sys
import os
import time

class Color:
    #Green -> green = "\033[92m" #Color.green
    #Yellow -> yellow = "\033[93m" #Color.yellow
    #Red -> red = "\033[91m" #Color.red
    #Blue -> blue ="\033[34m" #Color.blue
    #Purple -> purple = "\033[35m" #Color.purple
    #Turquoise -> turquoise = "\033[36m" #Color.turquoise
    bold = "\033[1m" #Color.bold
    reset = "\033[0m" #Color.reset

print("Do you want to "+Color.bold+"play again?"+Color.reset+"")
print("To exit type "+Color.bold+"\"exit\"."+Color.reset+ \
      "\nTo play again write "+Color.bold+"\"again\"."+Color.reset+"")

exit_or_again = input()

if exit_or_again == "exit" :
    time.sleep(1)
    sys.exit()
elif exit_or_again == "again" :
    time.sleep(1)
    print("\n\n<---------------NEW-TRY--------------->\n\n")
    os.execv(sys.executable, ["python"] + sys.argv)
else :
    print(Color.bold+"Give a correct answer."+Color.reset)
    time.sleep(1)
    print("\n\n"+Color.bold+\
    "<---------------NEW-TRY--------------->"+Color.reset+"\n\n")
    os.execv(sys.executable, ["python"] + sys.argv)
