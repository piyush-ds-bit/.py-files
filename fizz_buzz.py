

result=None
def fizz_buzz(number: int) -> str:
    """Returns `fizz` , `buzz` or `fizz_buzz` for the number divisible by `3` , `5` or by `both` """
    if number%3==0 and number%5==0:
        return "fizz_buzz"
    elif number%3==0:
        return "fizz"
    elif number%5==0:
        return "buzz"
    else:
        return "{}".format(number)





for i in range(1,101):
    print(" The number {0} is {1}".format(i,fizz_buzz(i)))
print(input("it's your call now: "))
