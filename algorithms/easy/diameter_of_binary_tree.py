#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找出leaf-to-leaf最長的距離
解題思路
1.設定一個diameter儲存最長距離
2.透過遞回找到左右子樹最深的距離
3.若兩者相加>原diameter,則更新diameter
TakeAway
- nonlocal:在巢狀結構內,能使用外層變數
- 加深recursion概念
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            
            diameter = max(diameter,left_path+right_path)
            return max(left_path,right_path)+1
        
        longest_path(root)
        return diameter
        
        
        