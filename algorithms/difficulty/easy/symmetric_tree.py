#############
# Author : Yujun Wen
# Last edit: 2022/6/21
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 檢查二元樹是否左右對稱
解題思路
1.透過Recursion一路比較下去
2.此解法參考discussion
TakeAway
- preorder、inorder、postorder都可以用此架構解
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)