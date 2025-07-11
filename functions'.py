# def multiply(x,y):
#     result=x*y
#     return result
#
# answer=multiply(10.5,4)
# print(answer)
#
# answer2=multiply(56,99.9)
# print(answer2)
# print()
#
# for val in range(1,6):
#     two_times=multiply(3,val)
#     print(two_times)
#
#
# def is_palindrome(string):
#     backward=string[::-1]
#     return backward.casefold()==string.casefold()
#
# word=input("Pls write your word: ")
# if is_palindrome(word):
#     print("{} is a Palindrome word.".format(word))
# else:
#     print("{} is not a Palindrome word.".format(word))
#
#
# def is_palindrome_sentence(string):
#     backward=string[::-1]
#     return backward.casefold().replace(" ","").replace("?","")==string.casefold().replace(" ","").replace("?","")
#
# word=input("Pls write your word: ")
# if is_palindrome_sentence(word):
#     print("{} is a Palindrome word.".format(word))
# else:
#     print("{} is not a Palindrome word.".format(word))


def is_palindrome_sentence(string):
    backward=string[::-1]
    return ''.join(char for char in backward.casefold() if char.isalnum())==''.join(char for char in string.casefold() if char.isalnum())

word=input("Pls write your word: ")
if is_palindrome_sentence(word):
    print("{} is a Palindrome word.".format(word))
else:
    print("{} is not a Palindrome word.".format(word))
