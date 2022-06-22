#############
# Author : Yujun Wen
# Last edit: 2022/6/23
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 驗證BST是否合法
解題思路
1.做任何的操作都要遵守BST的定義(左子樹的值不超過root,右子樹的值不小於root)
2.需要使用輔助函數,增加函數的參數清單,夾帶額外資訊,以解決問題
3.
TakeAway
- BST的定義
- 輔助函數的使用
- 二元樹的思考框架即為: 確定一個節點要做的事情後,剩下則透過遞迴完成
"""
# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            """
            兩個return 分別代表
            1.右子樹的值的high可以無限大,但是low一定要>= root
            2.左子樹的值的low可以無限大,但是high一定要<= root
            """
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)
            