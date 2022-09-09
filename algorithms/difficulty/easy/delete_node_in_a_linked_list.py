#############
# Author : Yujun Wen
# Last edit: 2022/7/2
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個node指向要刪除的節點,刪除他
解題思路
1. 直接用下個節點的屬性完全取代當前節點,就可以跨過去
TakeAway
- linked list的操作
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val 
        node.next = node.next.next 
        
        
            
        