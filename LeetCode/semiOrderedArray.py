def semiOrderedPermutation(nums):
        n = len(nums)
        perm = 0
        if nums[0] == 1 and nums[-1] == n:
            return perm
        
        one_index = nums.index(1)
        n_index = nums.index(n)

        perm = (n - n_index - 1) + (one_index)

        return perm-1 if one_index > n_index else perm



n = [4,1,2,3]

print(semiOrderedPermutation(n))