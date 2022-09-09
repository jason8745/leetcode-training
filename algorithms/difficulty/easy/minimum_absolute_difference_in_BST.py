#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- return the minimum absolute difference
解題思路
1.做inorder
2. [1,0,48,null,null,12,49] inorder-->[0,12,49,48,1]
TakeAway
- 直接暴力一個一個比也可以,但是時間複雜度較高
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root,output):
            if root == None:
                return 
            else:
                inorder(root.left, output)
                output.append(root.val)
                inorder(root.right, output)
        output=[]
        inorder(root,output)
        mini_diff = float('inf')
        for i in range(1,len(output)):
            mini_diff = min(mini_diff,output[i]-output[i-1])
        return mini_diff