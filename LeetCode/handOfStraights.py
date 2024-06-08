# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.



from collections import Counter

def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    
    count = Counter(hand)
    hand = sorted(hand)
    
    while hand:
        first = hand[0]
        
        for i in range(groupSize):
            if count[first + i] > 0:
                count[first + i] -= 1
                hand.remove(first + i)
            else:
                return False
    
    return True

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightHand(hand,groupSize))


def differentApproach(hand,groupSize):
    if len(hand) % groupSize != 0:
        return False

    hand.sort()
    n=len(hand)
    i = 0
    while(i<n):
        first = hand[i]
        group = range(first,first+groupSize)
        for num in group:
            if num not in hand:
                return False
            else:
                hand.remove(num)
        n=len(hand)
    return True

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(differentApproach(hand,groupSize))