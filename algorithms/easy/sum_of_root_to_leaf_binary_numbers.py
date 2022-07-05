#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 對樹做dfs後(preorder)回傳其值32進制的總和
解題思路
1.先寫下Visiting時要做甚麼
2.套入preorder的架構
TakeAway
- preorder的架構
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.root_to_leaf=0
        def preorder(r,curr_number):
            # visiting時的架構
            if r:
                curr_number = (curr_number << 1) | r.val
                # 走到底
                if not (r.left or r.right):
                    self.root_to_leaf += curr_number
                
                preorder(r.left,curr_number)
                preorder(r.right,curr_number)
        preorder(root,0)
        return self.root_to_leaf