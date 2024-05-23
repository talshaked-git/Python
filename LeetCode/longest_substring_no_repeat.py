# Problem: Given a string s, find the length of the longest substring without repeating characters.
# Example: s = "abcabcbb" → Output: 3 (substring "abc")

def longest_substring(s):
    start = 0
    end = 0
    max_length = 0
    set_characters = set()

    for end in range (len(s)):
        while s[end] in set_characters:
            set_characters.remove(s[start])
            start += 1
        set_characters.add(s[end])
        max_length = max(max_length, end-start +1)
    return max_length

s = "a"
print(longest_substring(s))
