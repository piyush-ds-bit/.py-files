Sankhya=int(input("Tell me: "))

# if Sankhya>=16 and Sankhya<=65:  #Another way below
#if 16<=Sankhya<=65:               #Another way below using RANGE
if Sankhya in range(16,66):
    print("Noice job...!")
else:
    print("Get lost.")

print("-"*80)
Digit=int(input("Type number= "))
if Digit<16 or Digit > 65:
    print("Hey there")
else:
    print("Namaskar")
