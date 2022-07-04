#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從BST中,找到在low和high之間的值,回傳其和
解題思路
1.做inorder
TakeAway
- inorder的操作框架就是LVR,在V的地方會放Visiting的時候要做的邏輯判斷,其他就是Traversal(尋訪)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        def inorder(t: TreeNode):
            if t:
                inorder(t.left)
                if t.val >=low and t.val<=high:
                    self.ans+=t.val
                inorder(t.right)
                
        inorder(root)
        return self.ans