#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到node=val,並回傳其子樹
解題思路
1.先寫出Visiting時要做什麼
2.search時有二分搜尋的味道
TakeAway
- 二元樹的特性
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val ==root.val:
            return root
        return self.searchBST(root.left,val) if val<root.val\
                else self.searchBST(root.right,val)
            
