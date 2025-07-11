# choose_items="-"
# computer_parts=[]
# while choose_items!="0":
#     if choose_items in "123456":
#         print("Adding no. {} item in your bucket:)".format(choose_items))
#         if choose_items=="1":
#             computer_parts.append("Computer")
#         elif choose_items=="2":
#             computer_parts.append("Monitor")
#         elif choose_items=="3":
#             computer_parts.append("Mouse")
#         elif choose_items=="4":
#             computer_parts.append("Study Desk")
#         elif choose_items=="5":
#             computer_parts.append("Keyboard")
#         elif choose_items=="6":
#             computer_parts.append("HDMI Cable")
#
#     else:
#         print("Please select the  available items:")
#         print("1: Computer")
#         print("2: Monitor")
#         print("3: Mouse")
#         print("4: Study Desk")
#         print("5: Keyboard")
#         print("6: HDMI Cable")
#         print("0: Finish")
#     choose_items=input()
# else:
#     print("Thank Aapka")
#     print("Ye rahe aapke items: {}".format(computer_parts))


available_items=["Computer",
                 "Monitor",
                 "Mouse",
                 "Study Desk",
                 "Keyboard",
                 "HDMI Cable",
                 "Printer",
                 "Adapter"
                 ]
valid_choice=[]
for i in range(1,len(available_items)+1):
    valid_choice.append(str(i))
print(valid_choice)
choose_items="-"
computer_parts=[]
while choose_items!="0":
    if choose_items in valid_choice:
        index=int(choose_items) - 1
        chosen_items = available_items[index]
        if chosen_items in computer_parts:
            computer_parts.remove(chosen_items)
            print("Removing no. {} item from your bucket:)".format(choose_items))
        else:
            computer_parts.append(chosen_items)
            print("Adding no. {} item in your bucket:)".format(choose_items))
    else:
        print("Please select the  available items:")
        for number,part in enumerate(available_items):
            print("{0}:  {1}".format(number+1,part))
    choose_items=input()
else:
    print("Thank Aapka")
    print("Ye rahe aapke items: {}".format(computer_parts))

#Some more ENUEMERATE examples.
# for index,character in enumerate("ayodhyapati"):
#     print(index,character)
