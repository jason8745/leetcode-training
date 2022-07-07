#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- determine if it is height-balanced.
- height-balance--> a binary tree in which the left and right subtrees of every node differ in height by no more than 1
解題思路
1.height會計算出最深的深度
2.preorder的架構
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left),height(node.right))
    
        if not root:
            return True
        # preorder的架構
        # visiting做是否height的判斷
        # 之後traversal 左子和右子 用return and 來總結最後的return
        return abs(height(root.left)-height(root.right))<2\
            and self.isBalanced(root.left)\
            and self.isBalanced(root.right)