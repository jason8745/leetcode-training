#############
# Author : Yujun Wen
# Last edit: 2022/6/19
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到二元樹最大深度
解題思路
1.找到最大深度-->DFS,使用Recursion
TakeAway
- 看到DFS可以直接考慮Recursion
- Recursion的寫法
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            # 空樹
            return 0
        if not root.left and not root.right:
            # 沒有葉子
            return 1
        # Recursion
        left_height = 1 + self.maxDepth(root.left)
        right_height = 1 + self.maxDepth(root.right)
        return max(left_height , right_height)