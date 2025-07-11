menu = [
    ["daal", "bhaat", "bhujiya"],
    ["bhaat", 'daal'],
    ["spam", "bhaat", "bhujiya"],
    ["daal", "chokha", "spam", "spam"],
    ["chokha", "chutney", "ghew", "aachar"],
    ["spam", "daal", "spam", "spam","achaar", "spam"],
]

# solution 1

for item in menu:
    for index in range(len(item)-1,-1,-1):
        if item[index]=="spam":
            del item[index]
    print(item)


print()
print()
print()
# solution 2

for item in menu:
    for i in item:
        if i != "spam":
            print(i,end=", ")
    print()
