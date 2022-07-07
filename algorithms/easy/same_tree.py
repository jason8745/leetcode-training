#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 判斷兩棵樹是否相同
解題思路
1.做inorder
2. 左子樹和右子樹都true才可以回傳true
TakeAway
- 架構上還是inorder,只是return綜合了左子和右子traversal的結果
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val!=q.val :
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)