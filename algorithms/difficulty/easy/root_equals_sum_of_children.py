#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 確認root的值是否為左、右子樹
解題思路
1.樹的操作
TakeAway
- 對樹狀結構的操作
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)