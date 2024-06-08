# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):
        ls = []
        if root.left == None and root.right == None:
            return 0
            
        self.traverseTree(root,ls)

        return sum(ls)


    def traverseTree(self,root,ls):
        if root.left != None:
            root.val = 0
            self.traverseTree(root.left,ls)
        if root.right != None:
            root.val = 0
            root.right.val = 0
            self.traverseTree(root.right,ls)
        
        ls.append(root.val)

