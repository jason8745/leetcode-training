#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- return mode value in the tree
解題思路
1.選擇inorder架構
TakeAway
- inorder的解題架構
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.max_count = 0
        self.current_count = 0 
        self.result = []
        def dfs(node):
            if not node: return
            # traversal
            dfs(node.left)
            # visiting(主要邏輯)
            self.current_count = 1 if node.val != self.prev else self.current_count + 1
            if self.current_count == self.max_count:
                self.result.append(node.val)
            elif self.current_count > self.max_count:
                self.result = [node.val]
                self.max_count = self.current_count
            self.prev = node.val
            # traversal
            dfs(node.right)
        dfs(root)
        return self.result