#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到LCA
解題思路
1.兩個值都大於root時就往右子樹找,兩個值都小於root時就往左子樹找
2.當只符合一個條件,就找到了
TakeAway
- BST中,左子樹都會小於root,右子樹會大於root
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        
        p_val = p.val
        q_val = q.val
        
        if p_val >parent_val and q_val >parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p_val<parent_val and q_val<parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root