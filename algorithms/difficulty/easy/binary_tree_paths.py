#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 列出所有從root到leaf的路徑
解題思路
1.有點難
2.主要邏輯就是碰到leaf就append進path,如果子樹還能走下去就append進stack,並進行字串的處理
TakeAway
- 努力理解
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths=[]
        stack=[(root,str(root.val))]
        while stack:
            node,path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left,path+'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right,path+'->'+str(node.right.val)))
                
        return paths