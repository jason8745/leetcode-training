#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 合併二元樹
解題思路
1.先列出基本case
2.Visiting的時候相加
TakeAway
- preorder、postorder、inorder操作
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None:
            return root2
        if root2==None:
            return root1
        
        t = TreeNode(root1.val+root2.val) # 只有一個值時就是代表val
        t.left = self.mergeTrees(root1.left,root2.left)
        t.right = self.mergeTrees(root1.right,root2.right)
        return t
