# i=0
# while i<10:
#     print("{}".format(i))
#     i+=1
from functools import update_wrapper
from idlelib.run import quitting

#  ADVENTURE GAME uses while loop to change direction
ways_to_go=["north","south","east","west"]
choosen_one=""
while choosen_one not in ways_to_go:
    choosen_one=input("Please,choosiye na: ")

print("Sahi pakre hai....rasta")
