#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 前序遍尋BT
解題思路
1.preorder的順序是root-->left-->right
TakeAway
- preorder
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(t):
            if t:
                preorder.append(t.val)
                dfs(t.left)
                dfs(t.right)
                
        preorder=[]
        dfs(root)
        return preorder