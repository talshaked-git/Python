
# Find the max sum subarray of a fixed size K
# Example input:
# [ 4, 2, 1 , 7 , 8, 1 , 2 ,8, 1 ,0]

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

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 3
print(MaxSumSubArray(arr, k))