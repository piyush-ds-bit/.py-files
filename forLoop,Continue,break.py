for i in range(1,11):
    for j in range(1,11):
        print("{0} times {1} is equals to {2}.".format(i,j,i*j))
    print("-"*88)

# LIST and CONTINUE & BREAk

Vivaah_list=["lehanga","Card","Makeup","Pandit ji","Atithi","Preparation"]
for item in Vivaah_list:
    print(item+"checked")

Vivaah_list=["lehanga","Card","Makeup","Pandit ji","Atithi","Preparation"]
for item in Vivaah_list:
    if item=="Pandit ji":       #or if item!="Pandit ji",then without continue statement,we can print same data as it isprinting now.
        continue
    print(item+" checked")

Vivaah_list=["lehanga","Card","Makeup","Pandit ji","Atithi","pakwaaan","Preparation"]
ItemToFind="Mama"
#foundAt= None
for index in range(len(Vivaah_list)):
    if Vivaah_list[index]==ItemToFind:
        foundAt=index
        break

print("Pakwaan is at position {}.".format(foundAt))
