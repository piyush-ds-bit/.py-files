sankhya=[23,456,67,100,200,175,99,288,301,111,234,521,309,69]
print(len(sankhya))
# del sankhya[:2]
# print(sankhya)
# del sankhya[10:]
# print(sankhya)

# another way to delete items from a list
min_value=100
max_value=350
for index, value in enumerate(sankhya):
    if (value<min_value) or (value>max_value):
        del sankhya[index]
print(sankhya)

#  this case is also not suitable to delete any items from a list because once you delete a item,
# index is reassigned to items ...but in loop it increases one by one....so it may include
# any unwanted item from the list due to error in indexing
#  let see some safe way to delete item from a list
