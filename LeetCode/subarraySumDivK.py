def subarraysDivByK(nums, k):
    count = 0
    if not nums:
        return count
    
    if nums[0] % k == 0:
        count+=1
    
    prefixA = []
    s = 0
    
    prefixA.append(nums[0])
    for i in range(1,len(nums)):
        prefixA.append(prefixA[i-1]+nums[i])
        if prefixA[i] % k == 0:
            count+=1
    
    for i in range(1,len(nums)):
        for j in range(i,len(nums)):
            s = prefixA[j] - prefixA[i-1]
            if s % k == 0:
                count += 1
            s = 0

    return count


# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums,k))


# Example 2:

# Input: nums = [5], k = 9
# Output: 0
nums = [5]
k = 9
print(subarraysDivByK(nums,k))