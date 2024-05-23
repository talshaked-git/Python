
def longestPalindrome(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    if s == s[::-1]:
        return s
    max_len = 0
    max_str = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
                    max_str = s[i:j]
    return max_str

s = "aacabdkacaa"
print(longestPalindrome(s)) # Output: "aca"
