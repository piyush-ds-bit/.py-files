Even=[2,4,6,8]
odd=[1,3,5,7,9]
Even.extend(odd)
print(Even)
Even.sort()
print(Even)
wakya=sorted("The quick brown fox jumps over the lazy dog",
             key=str.casefold)
print(wakya)
numbers=[2.1,5.6,7.89,1.9,0.5]
print(id(numbers))
numbers.sort()
print(id(numbers))
op=sorted(numbers)
print(id(op))
# .sort() method modify your present list or string into a list...whereas sorted() method creat a new list
# sand doesn't affect your previous list or string.For example
po="namaskaram sabko"
po.split()
print(po)
ko="namaskaram sabko"
ok=sorted(ko)
print(ok)
print(ko)

print()
omm=["Piyush","keya","Ravi","joe","ok","Hemnarayan"]
omm.sort()
print(omm)
# if two different list have same elements,then we can print them by
# print(list1==list2)
# print(list1 is list2)
# if you want to copy one list into another list , just type
# list2 = list2.(copy)
# print(list2)
