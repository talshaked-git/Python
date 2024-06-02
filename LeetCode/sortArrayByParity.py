
def SortArrayByParity(nums):
    even=[]
    odd=[]
    sortedL=[]

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    
    for i in range(len(even)):
        sortedL.append(even[i])
    
    for i in range(len(odd)):
        sortedL.append(odd[i])
    
    return sortedL


nums = [3,1,2,4]
print(SortArrayByParity(nums))