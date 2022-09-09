#############
# Author : Yujun Wen
# Last edit: 2022/7/5
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 找到樹中兩個節點相加=k 回傳true
解題思路
1.一看到就可以想到是binary_search
2.可以整合BST的特性來做到樹的binary_search
3.return 的處理
TakeAway
- 樹的binary search
- 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def binary_search(target):
            node = root
            while node:    
                if node.val>target:
                    node = node.left
                elif node.val<target:
                    node = node.right
                else:
                    return True, node
            return False, None
    
        def dfs(node):
            if not node:
                return False
            
            left_found = dfs(node.left) #traversal
            found, found_node = binary_search(k-node.val) #visiting
            right_found = dfs(node.right) #traversal

            return left_found | (found and found_node != node) | right_found
        
        return dfs(root)