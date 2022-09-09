#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 計算所有左子葉的合
解題思路
1.一開始沒思考到需要紀錄是否為左子樹的判斷
2. 使用preorder,在visiting的時候,只有是葉子且符合左子樹的值會被加進total,否則就會加0
TakeAway
- 架構上還是preorder
- traversal狀態的累積
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        
        def process_subtree(subtree,is_left):
            # visiting
            if not subtree.left and not subtree.right:
                return subtree.val if is_left else 0
            total=0
            # 把traversal的狀態記下來
            # 這裡代表非空就走,不然就不走
            if subtree.left:
                total += process_subtree(subtree.left,True)
            if subtree.right:
                total += process_subtree(subtree.right,False)
                
            return total
        
        return process_subtree(root,False)
            