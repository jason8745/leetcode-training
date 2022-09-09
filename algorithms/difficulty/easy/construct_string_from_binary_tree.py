#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- preorder traversal
解題思路
1.有點難
2.valuesum的主要功能是透過traversal時計算value總和,但在visiting的時候做Tilt的計算
TakeAway
- 從helper裡還是可以看出preorder的架構,但這題遇到左跟右的的做法有些微不同,所以需要調整
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        sb = [] # init string builder
        
        # helper function to create result
        def helper(node: TreeNode) -> None: 
            if not node:
                return
            # visiting
            sb.append(str(node.val))
            if not node.left and not node.right:
                # leaf node, stop processing
                return
            # traversal
            sb.append('(')          # always wrap left node with parenthesis when right node exist
            helper(node.left)       # process left node recursively 
            sb.append(')')                         
            
            # traversal
            if node.right:          # adding parenthesis for the right node only if it is not empty
                sb.append('(')
                helper(node.right)
                sb.append(')') 
        
        helper(root)

        return ''.join(sb)