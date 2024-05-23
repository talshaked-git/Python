# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example: nums = [2, 7, 11, 15], target = 9 → Output: [0, 1]

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            


nums = [2, 15, 1, 15]
target = 9
print(two_sum(nums, target)) # Output: [1, 2]



def different_approach (nums, target):
    d = {}
    n = len(nums)
    for i in range(n): #add nums list to the dictionary where the key is the number and the value is index in list
        d[nums[i]] = i 
    for j in range(n):
        ans = d.get(target - nums[j], -1)
        if ans != -1 and ans != j:
            return [j,ans]
        

print(f"different approach solution: {different_approach(nums,target)}")