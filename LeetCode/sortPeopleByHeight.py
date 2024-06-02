
def sortPeople(names, heights):
    sortedPpl = []
    sorted_heights = sorted(heights)[::-1]
    #sort heights by asencding order -> then return reversed list (basically sort by descending order)

    for height in sorted_heights:
        for i in range(len(names)):
            if heights[i] == height:
                sortedPpl.append(names[i])
                break

    return sortedPpl


names = ["Mary","John","Emma"]
heights = [180,165,170] 

print(sortPeople(names,heights))

names = ["Alice","Bob","Bobby"]
heights = [155,185,150]
print(sortPeople(names,heights))