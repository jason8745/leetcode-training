#############
# Author : Yujun Wen
# Last edit: 2022/7/4
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 有點看不懂題目
解題思路
1.(純對解題框架理解)
TakeAway
- inorder的操作框架就是LVR,在V的地方會放Visiting的時候要做的邏輯判斷,其他就是Traversal(尋訪)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c:TreeNode):
            if o:
                inorder(o.left,c.left)
                if o is target:
                    self.ans = c
                inorder(o.right,c.right)
        inorder(original,cloned)
        return self.ans