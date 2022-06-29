#############
# Author : Yujun Wen
# Last edit: 2022/6/28
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 給定一個Linked List(head 指向起點),每兩個相鄰的val做swap
解題思路
1.先新增一個dummy指標,其下一點指向head
2.
TakeAway
- 好難~先跳過
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        prev_node = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            # 常見的swap操作,只是換成了Linked List
            prev_node.next = second_node
            first_node.next = second_node.next 
            second_node.next = first_node
            
            prev_node = first_node
            head = first_node.next
            
            
        return dummy.next
        
        