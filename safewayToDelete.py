
# for ordered list

data=[4,5,100,104,105,110,120,130,150,160,170,183,185,187,188,191,200,350,370]
min_value=100
max_value=200

# process the low values in the list

stop=0
for index,value in enumerate(data):
    if value>=min_value:
        stop=index
        break
print(stop)  # for debugging
del data[:stop]
print(data)

# process the high value in the list
start=0
for index,value in enumerate(data):
    if value>=max_value:
        start=index
        break
print(start) # for debugging
del data[start+1:]
print(data)

# for unordered list
