

data=[100,104,105,4,110,120,130,66,150,370,160,170,183,185,399,187,188,191,200]
print(data)
min_value=100
max_value=190
for index in range(len(data)-1,-1,-1):
    print(index,data)
    if data[index] < min_value or data[index] > max_value:
         del data[index]

print(data)
# top_index=len(data)-1
# for index,value in enumerate(reversed(data)):
#     print(top_index-index,data)
#     if data[index]<min_value or data[index]>max_value:
#         del data[index]
# print(data)
