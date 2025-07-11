for i in range(1,5):
    print("No. {} squared is {} and cubed is {}.".format(i,i**2,i**3))
print("*"*50)

print()

for j in range(1,5):
    print("No. {} squared is {} and cubed is {}.".format(j,j**2,j**3))
    print("*"*50)

name=input("what is your name ? ")
age=int(input("How old are you,{0} ?".format(name)))
print("{} is {} years old.".format(name,age))

if age>=18:
    print("Jai Shree Ram")
else:
    print("radhe radhe")
