def SmallestPalindrom(s):
    if s == s[::-1]:
        return s
    n = len(s)
    s1 = list(s[0:(n//2):1])
    s2 = list(s[n:n//2-1:-1])
    
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            s1[i] = s2[i]
        elif s1[i] < s2[i]:
            s2[i] = s1[i]

    res = ''.join(s1+s2[::-1])
    return res


s = "seven"
print(SmallestPalindrom(s))