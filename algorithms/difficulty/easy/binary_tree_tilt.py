#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 計算tilt
解題思路
1.利用postorder(但應該都可以)
2.valuesum的主要功能是透過traversal時計算value總和,但在visiting的時候做Tilt的計算
TakeAway
- 有點分而治之的味道
- 當visiting要做的決定需要left和right的結果輔助時,就可以用這樣子return的方式
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt=0
        def valuesum(node):
            if not node: return 0
             # traversal(結合return就可以累積狀態)
            left_sum =valuesum(node.left)
             # traversal(結合return就可以累積狀態)
            right_sum =valuesum(node.right)
             # visiting(核心邏輯) 
            tilt = abs(left_sum-right_sum) 
            self.total_tilt +=tilt
            
            return left_sum+right_sum+node.val
        
        
        valuesum(root)
        return self.total_tilt
        