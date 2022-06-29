#############
# Author : Yujun Wen
# Last edit: 2022/6/16
# email: yujunwen0517@gmail.com
#####
"""
快速理解題意
- 判斷Linked List是有環還是無還
解題思路
1.使用快慢指標概念,快慢指標皆從head出發,但快指標每次比慢指標多走一步,若有環,則必定會相遇
2.不含還的話,快指標會搶先遇到null值
TakeAway
- 快慢雙指標適合判斷Linked List的問題
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast!=None and fast.next!=None :
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
        

        