#############
# Author : Yujun Wen
# Last edit: 2022/6/25
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 檢查一個Linked List 是否為palindrome(回文)
解題思路
1.將Linked List讀入list後,檢查其和[::-1]. 是否相同
TakeAway
- 指針的操作
- python list reverse的操作
"""
# Definition for a binary tree node.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        point = head
        while point is not None:
            vals.append(point.val)
            point = point.next
        return vals ==vals[::-1]