#############
# Author : Yujun Wen
# Last edit: 2022/7/7
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 判斷給定的兩個node是否具有相同深度且擁有不同的parents
解題思路
1.一看到比深度就可以先考慮bfs
2.有點難直接看了答案
3.如果具有相同深度,但同一個parent就是siblings,不同parent就是cousins
TakeAway
- bfs常搭配queue
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([root])
        
        while queue:
            siblings=False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):
                node = queue.popleft()
                
                if not node:
                    siblings= False
                else:
                    # preorder架構
                    # visitng
                    if node.val==x or node.val==y:
                        if not cousins:
                            siblings,cousins=True,True
                        else:
                            return not siblings
                    # traversal
                    if node.left:
                        queue.append(node.left)
                    # traversal
                    if node.right:
                        queue.append(node.right)
                        
                    queue.append(None)
            if cousins:
                return False
            
        return False
        