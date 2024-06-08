# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

def replaceWords(dictionary, sentence):
    res = ""
    s_list = sentence.split(' ')
    changed = False

    for word in s_list:
        changed = False
        for i in range(len(word)):
            subword = word[0:i+1:]
            if subword in dictionary:
                changed = True
                res += subword
                res += ' '
                break
        if not changed:
            res += word
            res += ' '
    
    return res.strip()


# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary,sentence))