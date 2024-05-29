
INT_MIN = -2**31

# Using Kadane's Algorithm
def maxSubarray(arr):
    maxSum = INT_MIN
    currSum = 0

    for i in range(len(arr)):
        currSum += arr[i]
        
        if (maxSum < currSum):
            maxSum = currSum
        
        if (currSum < 0):
            currSum = 0
    
    return maxSum


nums = [-2,-3,4,-1,-2,1,5,-3]

print(maxSubarray(nums))