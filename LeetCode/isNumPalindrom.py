
import math


def isPalindrome(number):
    return str(number) == str(number)[::-1]

print(isPalindrome(121))


# Checking if number is Palindrome without converting to string
def isNumPalindrome(number):
    res = int(number != 0) and ((number % 10) * (10**int(math.log(number,10))) + isNumPalindrome(number //10)) 
    return res == number

print (isNumPalindrome(121))