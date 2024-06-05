def firstCompleteIndex(arr, mat):
    m=len(mat) #
    n=len(mat[0])

    kdic= {}
    
    for i in range(m*n):
        for row in range(m):
            try:
                ele_i = mat[row].index(arr[i])
                kdic[("row",row)] = kdic.get(("row",row),0)+1
                kdic[("col",ele_i)] = kdic.get(("col",ele_i),0)+1
                if kdic[("row",row)] == n or kdic[("col",ele_i)] == m:
                    return i
                break
            except:
                continue

arr = [1,3,4,2]
mat = [[1,4],[2,3]]
print(firstCompleteIndex(arr,mat))

arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]
print(firstCompleteIndex(arr,mat))

    # [[1,2,3],
    #  [4,5,6],
    #  [7,8,9]]
    #  paint element 7 index=[2,0]
    #  kdic: ("row", 2): 1
    #  kdic: ("col", 0): 1
    #  paint element 8 index=[2,1]
    #  kdic: ("row", 2): 2
    #  kdic: ("col", 1): 1
    #  paint element 9 index=[2,2]
    #  kdic: ("row", 2): 3
    #  kdic: ("col", 2): 1