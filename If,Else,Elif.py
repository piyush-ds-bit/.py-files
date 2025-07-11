# name="QWQQQQSaloni ji"
# age=int(input("Aapka aayu,{} ? ".format(name)))
# if age <22:
#     print("Chhoti bachhi ho kya?")
# elif age ==22:
#     print("Janmdin ki anant mangalkamnaye")
# else:
#     print("Badi bachhi ho kya?")
#
#
#
# answer=69
# Guess=int(input("Guess your number: "))
# if Guess<answer:
#     print("Please,think higher...!")
#     Guess=int(input("Guess your number: "))
#     if Guess==answer:
#         print("You got it.")
#     else:
#         print("Better luck next time!")
# elif Guess >answer:
#     print("Please,think lower...!")
#     Guess=int(input("Guess your number: "))
#     if Guess==answer:
#         print("You got it.")
#     else:
#         print("Better luck next time!")
# else:
#     print("Badhai ho")
#
# # As you can see,in the above code,we had to duplicate/rewrite a block a code to command something,
# # but there is always a second way to remove this overwriting
# # For this,we can USE != sign.....see below
#
# answer=23
# Guess=int(input("Guess your number: "))
# if Guess!=answer:
#     if Guess<answer:
#         print("Guess higher value")
#     else:
#         print("Guess lower value")
#     Guess=int(input("Final chance: "))
#     if Guess==answer:
#         print("You got it.")
#     else:
#         print("Better luck next time")
# else:
#     print("Badhai Ho...!")

import random

def get_integer(prompt):
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)

Upto=1000
answer=random.randint(1,Upto)
# print("Your secret answer is: {}.".format(answer))
print("Guess your number upto {}: ".format(Upto))
Guess=0
while Guess!=answer:
    Guess=get_integer(": ")

    if 0<Guess<answer:
        print("Guess higher value")
    if Guess>answer:
        print("Guess lower value")
    else:
        if Guess==answer:
            print("Yeah..finally,you got it")
            break
        if Guess==0:
            print("Thank You")
            break
    Guess=int(input("Another chance: "))

else:
    print("Yeah...,You got it!")















print()
