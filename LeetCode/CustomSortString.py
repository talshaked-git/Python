
def SortStringByOrder(order, s):
    sortedS = ''

    for let in order:
        for i in range(len(s)):
            if s[i] == let:
                sortedS+=(s[i])

    for i in range(len(s)):
        if s[i] not in order:
            sortedS+=(s[i])

    return sortedS


order="bcafg"
s="abcdkk"

print(SortStringByOrder(order,s))