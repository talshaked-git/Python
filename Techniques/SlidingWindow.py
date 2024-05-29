
# Find the max sum subarray of a fixed size K (fixed size window)
# Example input:
# [ 4, 2, 1 , 7 , 8, 1 , 2 ,8, 1 ,0], k = 3
INT_MAX = 2**31 - 1
INT_MIN = -2**31

def MaxSumSubArray(arr, k):
    if len(arr) < k:
        return []
    currentSum = 0
    maxSum = INT_MIN

    for i in range(len(arr)):
        currentSum += arr[i]
        if (i >= k -1 ):
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[i - (k - 1)]
    
    return maxSum

arr = [-1, 2, 3, 1, -3, 2]
k = 2
print(MaxSumSubArray(arr, k))


# Find the smallest subarray with given sum (dynamic window)
# Example input:
# [4, 2, 2, 7, 1, 1, 2, 2, 1, 0], sum = 8

def smallestSubarray(arr, sum):
    currentWindowSum = 0
    windowStart = 0
    minWindowSize = INT_MAX
    for windowEnd in range(len(arr)):
        currentWindowSum += arr[windowEnd]

        while(currentWindowSum >= sum):
            minWindowSize = min(minWindowSize,windowEnd - windowStart + 1)
            currentWindowSum -= arr[windowStart]
            windowStart += 1
    
    return minWindowSize



arr = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
sum = 8
print(smallestSubarray(arr, sum))



# Find the longest substring length with k distinct characters
# Example input:
# s = "AAAHHIBC", k = 