#############
# Author : Yujun Wen
# Last edit: 2022/7/8
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- find its minimum depth
解題思路
1.使用postorder
2.主要是深度的計算,traversal時要+1
TakeAway
- postorder的解題架構
- 邏輯計算,感覺也可以先sort再找第二個

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,d):
            if not node:
                return 0
            
            left =dfs(node.left,d+1)
            right = dfs(node.right,d+1)
            # 走到leaf時
            if not node.left and not node.right:
                return d
            
            if left and right:
                return min(left,right)
            
            return left or right
        
        return dfs(root,1)
        
        
        