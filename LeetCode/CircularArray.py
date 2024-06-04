
def circular(sentence):

    words = sentence.split()
        
    if words[-1][-1] != words[0][0]:
        return False

    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            return False
    
    return True
        

print(circular("Leetcode is cool"))



def circular2nd(sentence):

    words = sentence.split()
    n = len(words)
    for i in range(n):
        if words[i][-1] != words[(i+1)%n][0]:
            return False
    
    return True

print(circular("Leetcode is cool"))