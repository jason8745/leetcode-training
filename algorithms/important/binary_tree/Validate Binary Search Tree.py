#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key
"""

# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower,upper,node):
            if not node:
                return True
            elif node.val<=lower or node.val>=upper:
                return False
            else:
                return dfs(lower,node.val,node.left) and dfs(node.val,upper,node.right)
        return dfs(float('-inf'),float('inf'),root)


        
        
