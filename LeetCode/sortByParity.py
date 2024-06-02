def sortByParity(nums):
    x_ev = []
    y_od = []
    sorted_list=[]
    for i in range (len(nums)):
        if nums[i] % 2 == 0:
            x_ev.append(nums[i])
        else:
            y_od.append(nums[i])
    
    for i in range (len(nums)):
        if i % 2 == 0:
            sorted_list.append(x_ev.pop())
        else:
            sorted_list.append(y_od.pop())

            
    return sorted_list

nums = [4, 2, 5, 7, 1, 2, 3, 4]
print(sortByParity(nums))