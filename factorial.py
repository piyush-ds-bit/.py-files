def factorial(number):
    if 0<=number<=1:
        return 1
    else:

        for f in range(1,number+1):
            result=1*f

        return result

for i in range(0,36):
    print(i,factorial(i))
