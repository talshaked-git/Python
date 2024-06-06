def findPeaks(mountain):
    res = []
    
    for i in range(1,len(mountain)-1):
        if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
            res.append(i)
    
    return res