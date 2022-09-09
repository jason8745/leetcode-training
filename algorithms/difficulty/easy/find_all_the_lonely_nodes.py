#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找lonely node
解題思路
1.做dfs(三種order都可以)
TakeAway
- preorder、postorder、inorder操作
- DFS概念
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def inorder(t: TreeNode):
            if t:
                # traversal
                inorder(t.right)
                # visiting
                if not t.left and  t.right:
                    self.ans.append(t.right.val)
                if t.left and not t.right:
                    self.ans.append(t.left.val)
                # traversal
                inorder(t.left)
            
        inorder(root)
        return self.ans

# postorder
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def postorder(t: TreeNode):
            if t:
                postorder(t.right)
                postorder(t.left)
                if not t.left and  t.right:
                    self.ans.append(t.right.val)
                if t.left and not t.right:
                    self.ans.append(t.left.val)
                
            
        postorder(root)
        return self.ans


#preorder
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def preorder(t: TreeNode):
            if t:
                if not t.left and  t.right:
                    self.ans.append(t.right.val)
                if t.left and not t.right:
                    self.ans.append(t.left.val)
                preorder(t.right)
                preorder(t.left)
                
            
        preorder(root)
        return self.ans