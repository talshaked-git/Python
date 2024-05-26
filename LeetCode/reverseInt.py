INT_MAX = 2**31 - 1
INT_MIN = -2**31

def reverse(num):
    if num == 0:
        return 0
    
    neg = 1
    reversedNum = 0

    if num < 0:
        neg = -1
        num *= -1

    while (num != 0):
       dig = num % 10
       reversedNum = reversedNum * 10 + dig
       num //= 10

    if neg:
        reversedNum *= -1
    
    return reversedNum if INT_MIN <= reversedNum <= INT_MAX else 0 ### guruantee that result is signed 32-bit int 

print(reverse(-1243))