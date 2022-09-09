#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 確認兩棵樹的leaf是否相同
解題思路
1.先列出case
2.使用preorder
TakeAway
- ans+=dfs(root.left)的用法
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            ans=[]
            if not root:return []
            if not root.left and not root.right:
                ans.append(root.val)
            ans+=dfs(root.left)
            ans+=dfs(root.right)
            return ans
        
        return dfs(root1)==dfs(root2)