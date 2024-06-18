def maxProfitAssignment(difficulty, profit, worker):
    both = sorted(zip(difficulty, profit))
    worker.sort()

    res = 0
    cur_prof = 0
    i = 0
    n = len(both)
    
    for wrk in worker:
        while i < n and wrk>=both[i][0]:
            cur_prof = max(cur_prof, both[i][1])
            i += 1
        res += cur_prof

    return res



# Example 1:

# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately..
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(maxProfitAssignment(difficulty, profit, worker))
# Example 2:

# Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# Output: 0
difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]
print(maxProfitAssignment(difficulty, profit, worker))