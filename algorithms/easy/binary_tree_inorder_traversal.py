#############
# Author : Yujun Wen
# Last edit: 2022/6/21
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 中序遍歷二元樹
解題思路
1.inorder是會先拜訪左子節點,再拜訪父節點,最後拜訪右子節點
2.此解法參考discussion
TakeAway
- preorder、inorder、postorder都可以用此架構解
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            in_order.append(node.val)
            dfs(node.right)
        
        in_order = []
        dfs(root)
        return in_order
            
        

        