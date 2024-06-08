# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        seq1 = []
        seq2 = []
        self.traverseTree(root1,seq1)
        self.traverseTree(root2,seq2)
        print(seq1)
        print(seq2)
        return seq1 == seq2


    def traverseTree(self, root, seq):
        if root.left != None:
            self.traverseTree(root.left,seq)
            
        if root.right != None:
            self.traverseTree(root.right,seq)
            
        if(root.left == None and root.right == None):
            seq.append(root.val)

