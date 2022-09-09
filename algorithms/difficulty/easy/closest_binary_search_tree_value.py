#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 回傳tree中和target最相近的值
解題思路
1.做inorder
2. 使用mi紀錄最小值,使用n紀錄最小值的n
TakeAway
- 架構上還是inorder,只是return綜合了左子和右子traversal的結果
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.mi = float('inf')
        self.n =None
        def inorder(t):
            
            if t:
                if abs(target-t.val)<self.mi:
                    self.n=t.val
                    self.mi = abs(target-t.val)
                
                inorder(t.left)
                inorder(t.right)
        inorder(root)
        return self.n
        