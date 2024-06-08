# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

def checkSubarraySum(nums, k):
    if len(nums)<=1:
        return False
    currSum = 0
    for i in range(len(nums)):
        currSum +=nums[i]
        for j in range(i+1,len(nums)):
            currSum +=nums[j]
            if currSum % k == 0:
                return True
        currSum = 0
    return False


# Input: nums = [23,2,4,6,7], k = 6
# Output: true
nums = [23,2,4,6,7]
k = 6
print(checkSubarraySum(nums,k))


# Input: nums = [5,0,0,0], k = 3
# Output: true
nums = [5,0,0,0]
k = 3
print(checkSubarraySum(nums,k))