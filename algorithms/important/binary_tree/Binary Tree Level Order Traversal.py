#############
# Author : Yujun Wen
# Last edit: 2022/9/7
# email: yujunwen0517@gmail.com
#####
"""
Note
1.做level order
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node,level):
            if len(levels)==level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
                
        helper(root,0)
        
        return levels

# Solution2
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        def dfs(node,level):
            if not node: return
            d[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
            
        dfs(root,0)
        return d.values()

# time complexity O(N)
# Space complexity O(N)
        
        
