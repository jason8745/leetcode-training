#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 後續遍尋BT
解題思路
1.postorder是會先拜訪左子節點,再拜訪父節點,最後拜訪右子節點
TakeAway
- 樹的尋訪
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            post_order.append(node.val)
        
        post_order = []
        dfs(root)
        return post_order
            