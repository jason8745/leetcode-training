#############
# Author : Yujun Wen
# Last edit: 2022/7/8
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- if root-to-leaf ==target return true
解題思路
1.當走到leaf時,就回傳targetSum是否為0的結果
2.左右只要有其一答成就好,所以用or 
TakeAway
- preorder的解題架構
- 利用return 來集成最後的狀態判斷

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        
        targetSum -=root.val
        if not root.left and not root.right:
            return targetSum==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        