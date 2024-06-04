

def distanceToTarget(words, target, startIndex):
    if target not in words:
        return -1
        
    n = len(words)
    
    stepsForward = 0
    stepsBackward = 0

    for i in range(n):
        stepsForward = (startIndex + i) % n
        stepsBackward = (startIndex - i + n) % n

        if words[stepsForward] == target or words[stepsBackward] == target:
            return i
    
    return -1



words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1

print(distanceToTarget(words,target,startIndex))