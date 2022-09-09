#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 計算每一level的平均值
解題思路
1.一看到的瞬間就會想到BFS
TakeAway
- BFS的寫法(要再研究)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        res=[]
        while queue:
            level_len = count = len(queue)
            level_sum=0
            while count:
                node = queue.popleft()
                level_sum +=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count-=1
            res.append(level_sum/level_len)
        return res
        