day="tuesday"
temperature=41
raining=True
if day=="Saturday" and temperature>40 or  raining:
    print("Welcome to Mandir")
else:
    print("Kya hua,phir naya bahana?")

print("-"*80)

name=input("Enter your name: ")
if name=="":
    print("aap Gumnaam hai kya")
else:
    print("Namaskaram,{} ji!".format(name))

print("-"*80)

Height=float(input("Enter Your height,plz: "))
Weight=int(input("Enter Your Weight,plz: "))
BMI=format(float(Weight/(Height*Height)),".2f")
print("Your BMI is {} .\nAnd\n".format(BMI))
if BMI<="18.5":
    print("You need some Cookies")
elif BMI>="25":
    print("Hey,Go and Run")
else:
    print("Now,that's a well maintained Body")
