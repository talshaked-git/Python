# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

# Return the largest possible value of num after any number of swaps.


def largestInteger(num):
    numS = list(str(num))
    
    for i in range(len(numS)):
        dig1 = int(numS[i])
        for j in range(i+1, len(numS)):
            dig2 = int(numS[j])
            if dig1 < dig2 and (dig1 % 2) == (dig2 % 2):
                numS[i], numS[j] = numS[j], numS[i]
                dig1 = int(numS[i])
    
    return int("".join(numS))

num = 5579
print(largestInteger(num)) #expected output 9755

num = 193154728
print(largestInteger(num)) #expected output 975318142