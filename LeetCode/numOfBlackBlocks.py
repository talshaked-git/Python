import collections

def countBlackBlocks(m, n, coordinates):
    res = [0,0,0,0,0]
    sum = 0
    numOfblocks = (n-1)*(m-1)
    # [0,0,0,0,0]
    # [0,0] = 2 | [0,1] = 2
    # [1,0] = 1 | [1,1] = 1
    blocks = collections.defaultdict(int)
    for cord in coordinates:
        if cord[0]<m-1 and cord[1]<n-1:
            blocks[(cord[0],cord[1])] +=1
        if cord[0]>0 and cord[1]<n-1 :
            blocks[(cord[0]-1,cord[1])]+=1
        if cord[1]>0 and cord[0]<m-1:
            blocks[(cord[0],cord[1]-1)]+=1
        if cord[1]>0 and cord[0]>0 :
            blocks[(cord[0]-1,cord[1]-1)]+=1
    ind = 0
    
    for ind,i in enumerate(blocks.values()):
        res[i]+=1
    if len(coordinates) != 0:
        if ind<numOfblocks:
            res[0] = numOfblocks -ind -1
    else:
        res[0] = numOfblocks

    return res

m = 3
n = 3
coordinates = [[0,0],[1,1],[0,2]]

print(countBlackBlocks(m,n,coordinates))