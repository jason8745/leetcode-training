#############
# Author : Yujun Wen
# Last edit: 2022/7/8
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- return true if there is a subtree of root with the same structure and node values
解題思路
1.一樣套上解題架構
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
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if t is None: return True
        def dfs(p, q):
            # visiting
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False
            # traversal
            return dfs(p.left, q.left) and dfs(p.right, q.right)        
        
        def find(s, t):
            # visiting
            if s is None: return False
            if dfs(s, t): return True
            # traversal
            return find(s.left, t) or find(s.right, t)
        
        return find(s, t)