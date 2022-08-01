#############
# Author : Yujun Wen
# Last edit: 2022/8/1
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 從以排序的link list中 移除重複的值
解題思路
- 使用雙指標操作
TakeAway

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return head
        
        current = head.next
        prev = head
        
        while current  != None:
            if current.val ==prev.val:
                prev.next = current.next
                current = current.next
                
            else:
                current = current.next
                prev = prev.next
                
        return head
        
        
        