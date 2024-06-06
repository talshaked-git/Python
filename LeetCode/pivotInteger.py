# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

def pivotInt(n):
    for i in range(1, n+1):
        sum_left = sum(range(1,i+1))
        sum_right = sum(range(i,n+1))
        if sum_left == sum_right:
            return i
    
    return -1

n = 8
print(pivotInt(n)) #expected 6: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

n = 9
print(pivotInt(n)) #expected -1: no pivot integer for 9


def differentApproach(n): #much faster
    r_sum = sum(i for i in range(n + 1))
    l_sum = 0
    for i in range(1, n + 1):
        l_sum += i
        if r_sum == l_sum:
            return i
        r_sum -= i
    return -1

n = 8
print(differentApproach(n)) #expected 6: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

n = 9
print(differentApproach(n)) #expected -1: no pivot integer for 9