#############
# Author : Yujun Wen
# Last edit: 2022/6/30
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個升幕的array,建立一個高度平衡的二元樹
解題思路
1.從正中間挑選root
2.當left>right時,代表沒有元素了
3.使用preorder Traversal
TakeAway
- tree的操作
- preorder使用
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left >right:
                return None
            
            p = (left+right)//2
            # preorder traversal
            root = TreeNode(nums[p])
            root.left = helper(left,p-1)
            root.right = helper(p+1,right)
            return root
        return helper(0,len(nums)-1)
        