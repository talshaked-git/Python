# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

# Return the number of integer points on the line that are covered with any part of a car.

def numberOfPoints(nums):
    ars = []
    for cord in nums:
        for i in range(cord[0],cord[1]+1):
            if i not in ars:
                ars.append(i)        
    return len(ars)




# Input: nums = [[3,6],[1,5],[4,7]]
# Output: 7
nums = [[3,6],[1,5],[4,7]]
print(numberOfPoints(nums))


# Input: nums = [[1,3],[5,8]]
# Output: 7

nums = [[1,3],[5,8]]
print(numberOfPoints(nums))