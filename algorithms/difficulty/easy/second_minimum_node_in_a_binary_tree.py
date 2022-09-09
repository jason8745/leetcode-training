#############
# Author : Yujun Wen
# Last edit: 2022/7/8
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個特定的樹(符合:root.val = min(root.left.val, root.right.val)),找到第二小的樹
解題思路
1.一樣套上解題架構
TakeAway
- preorder的解題架構
- 邏輯計算,感覺也可以先sort再找第二個

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                # visiting
                uniques.add(node.val)
                # traversal
                dfs(node.left)
                dfs(node.right)
                
        uniques=set()
        dfs(root)
        # 邏輯計算,感覺也可以先sort再找第二個
        min1,ans = root.val,float('inf')
        for v in uniques:
            if min1<v<ans :
                ans=v
        return ans if ans <float('inf') else -1