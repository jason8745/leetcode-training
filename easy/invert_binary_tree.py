#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- invert 一個二元樹
解題思路
1.將左右子樹都invert
TakeAway
- 決定好對root節點做的事後,剩下的交給recursion
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        # invert
        root.left = right
        root.right = left
        return root