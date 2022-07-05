#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 判斷樹每個節點的值是否都相同
解題思路
1.利用set
2.先做完一遍tree的尋訪,visiting時把值加進set()
3.最後判斷set的值是否超過1
TakeAway
- set()
- 樹的尋訪
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        seen =set()
        
        def inorder(t):
            if t :
                inorder(t.left)
                # visiting
                seen.add(t.val)
                inorder(t.right)
            
        
        inorder(root)
        return len(seen)==1
        
        