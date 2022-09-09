#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
ancestor: 祖先
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node):
            if not node:
                return False
            # postorder的解題架構
            left = dfs(node.left)
            right = dfs(node.right)
            # visit 主程式區
            cur = node ==p or node==q
            if (left and right) or (cur and right) or (cur and left):
                self.ans = node
                return
            return left or right or cur
        dfs(root)
        return self.ans

# time complexity O(N)
# Space complexity O(N)
        
        
