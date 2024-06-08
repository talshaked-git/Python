def findMinMoves(self, machines):
    s = sum(machines)
    n = len(machines)
    target = s // n  # average value of the array
    if target * n != s:
        return -1
    
    last_shift = 0
    res = 0
    for i in range(n):
        shift = last_shift + machines[i] - target
        if last_shift < 0 < shift:
            res = max(res, (shift - last_shift))
        else:
            res = max(res, abs(shift))
        last_shift = shift
    return res


# Input: machines = [1,0,5]
# Output: 3
# Explanation:
# 1st move:    1     0 <-- 5    =>    1     1     4
# 2nd move:    1 <-- 1 <-- 4    =>    2     1     3
# 3rd move:    2     1 <-- 3    =>    2     2     2
machines = [1,0,5]
print(findMinMoves(machines))