def maximumTripletValue(nums):
    triplets = []
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                triplets.append((i,j,k))
    maxV = -2**31
    
    for x,y,z in triplets:
        maxV = max(maxV,((nums[x]-nums[y])*nums[z]))
    
    return maxV if maxV>0 else 0



# Example 1:

# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 
nums = [12,6,1,2,7]
print(maximumTripletValue(nums))
# Example 2:

# Input: nums = [1,10,3,4,19]
# Output: 133
# Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
# It can be shown that there are no ordered triplets of indices with a value greater than 133.
nums = [1,10,3,4,19]
print(maximumTripletValue(nums))# Example 3:

# Input: nums = [1,2,3]
# Output: 0
# Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
nums = [1,2,3]
print(maximumTripletValue(nums))