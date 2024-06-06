# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.

# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.

# The bag initially contains:

# numOnes items with 1s written on them.
# numZeroes items with 0s written on them.
# numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.


def MaxSumOfKItems(numOnes,numZeros,numNegOnes, k): #Naive solution
    if k == 0:
        return 0
    res=0
    for i in range(numOnes):
        if k == 0:
            return res
        res+= 1
        k -= 1
    
    for i in range(numZeros):
        if k==0:
            return res
        k -= 1
    
    for i in range(numNegOnes):
        if k==0:
            return res
        res -= 1
        k -= 1
    return res
        
# Example 1:
# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
# Output: 2
# Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
# It can be proven that 2 is the maximum possible sum.
numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
print(MaxSumOfKItems(numOnes,numZeros,numNegOnes,k))

# Example 2:
# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
# Output: 3
# Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
# It can be proven that 3 is the maximum possible sum.
numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4
print(MaxSumOfKItems(numOnes,numZeros,numNegOnes,k))


def differentApproach(numOnes,numZeros,numNegOnes,k):
    allItems =[]
    allItems += [1]*numOnes
    allItems += [0]*numZeros
    allItems += [-1]*numNegOnes
    res = 0
    for i in range(k):
        res += allItems[i]
    
    return res


numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
print(differentApproach(numOnes,numZeros,numNegOnes,k))

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4
print(differentApproach(numOnes,numZeros,numNegOnes,k))