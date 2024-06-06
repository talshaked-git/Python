# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].

def countSymmetricIntegers(low, high):
    res = 0
    for x in range(low,high+1):
        strx = str(x)
        n = len(strx) 
        if n % 2 != 0:
            continue
        n //= 2
        x1 =list(strx[0:n:])
        x2 =list(strx[n::])
        sum1 = sum(list(map(int, x1)))
        sum2 = sum(list(map(int, x2)))
        if sum1 == sum2:
            res += 1
        
    return res


low = 1
high = 100
print(countSymmetricIntegers(low,high)) #expected 9

low = 1200
high = 1230
print(countSymmetricIntegers(low,high)) #expected 4